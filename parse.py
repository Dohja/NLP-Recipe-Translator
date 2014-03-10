import nltk
import fractions

def processIngredients(ingText, ingDict, measures):
    ingredients = {}
    # Ingredients will look something like this
##    4 skinless, boneless chicken breast halves
##    cayenne pepper, or to taste
##    salt
##    ground black pepper to taste
##    all-purpose flour for dredging
##    2 tablespoons olive oil
##    1 tablespoon capers, drained
##    1/2 cup white wine
##    1/4 cup fresh lemon juice
##    1/4 cup water
##    3 tablespoons cold unsalted butter, cut in
##    1/4-inch slices
##    2 tablespoons fresh Italian parsley, chopped
    ingList = ingText.split('\n')
    for ingredient in ingList:
        ingredients = processOneIngredient(ingredient, ingDict, ingredients, measures)
    return ingredients

def processOneIngredient(ing, ingDict, allIng, measures):
    solution = {}
    tokens = nltk.PunktWordTokenizer().tokenize(ing)
    if tokens == []: return allIng
    else:
        
        desc, name, prep = extractIngredient(tokens, ingDict)
        num, units = extractQM(tokens, ingDict, measures)
        weight = calculateWeight(name, ingDict, num, units)

    allIng[name] = {"name": name,
                    "weight": weight,
                    "quantity": num,
                    "measurement": units,
                    "description": desc,
                    "preparation": prep}
    return allIng


def extractQM(words, inDict, measures):
    quantity = None
    measurement = None
    for i in range(len(words)):
        if type(words[i]) == int or type(words[i]) == float:
            quantity = words[i]
        if words[i] in measures and words[i-1] == quantity:
            measurement = words[i]
            break

            ### this allows us to account for parentheticals, such that 1 (4.5 ounce) can mushrooms
            ### outputs 4.5 ounce as its amount and unit, and can becomes part of the description
            ### it will also cut off the program after 1 tbsp but not the above
        
    return [quantity, measurement]

def extractIngredient(tokens, ingDict):
    descriptor = None
    prep = None
    name = " ".join(tokens)
    for i in range(len(tokens)):
        descriptor = " ".join(tokens[:i])
        nameables = substringer(tokens[i:]) # ingredients that start with this word
        matches = [names for names in nameables if names in ingDict.keys()]
        if len(matches) > 0:
            name = matches.pop()
            lastNameable = nameables.pop()
            if lastNameable != name:
                prep = lastNameable[len(name):]
                if prep[0] == ',': prep = prep[2:]
            break
    return [descriptor, name, prep]

def substringer(words):
    substring = words[0]
    out = [words[0]]
    for i in words[1:]:
        substring = substring + " " + i
        out.append(substring)
    return out

def calculateWeight(name, ingDict, amount, unit):
    std = ingDict[name].stdMeasure.split()
    stdAmt = float(std[0])
    stdU = std[1]
    if stdU == unit: return amount/std
    else: return convertWeight(amount, unit, std, stdU)

def convertWeight(amount, unit, stdAmt, stdUnit):
    if amount == 0: return 0
    if unit == None or stdUnit == None or stdAmt == None: return 1
    if stdUnit == 'teaspoon':
        if unit in ['tsp', 'teaspoon', 'teaspoons']:
            return amount / stdAmt
        elif unit in ['tbsp', 'tbs', 'tablespoon', 'tablespoons']:
            return 3.0 * amount / stdAmt
        elif unit in ['pinch', 'dash']: return 0.25
        elif unit in ['c', 'cup', 'cups']:
            return 48.0 * amount/stdAmt
        elif unit in ['pint', 'pt', 'pints']:
            return 96.0 * amount/stdAmt
        elif unit in ['quart', 'quarts', 'qt']:
            return 192.0 * amount/stdAmt
        elif unit in ['gallon', 'gal', 'gallons']:
            return 768.0 * amount/stdAmt
        else:
            print "we can't easily convert from " + unit + " to " + stdUnit
            return 1
    elif stdUnit == 'tablespoon':
        if unit in ['tsp', 'teaspoon', 'teaspoons']:
            return (amount / stdAmt) / 3
        elif unit in ['tbsp', 'tbs', 'tablespoon', 'tablespoons']:
            return amount / stdAmt
        elif unit in ['pinch', 'dash']: return 0.01
        elif unit in ['c', 'cup', 'cups']:
            return 16.0 * amount/stdAmt
        elif unit in ['pint', 'pt', 'pints']:
            return 32.0 * amount/stdAmt
        elif unit in ['quart', 'quarts', 'qt']:
            return 64.0 * amount/stdAmt
        elif unit in ['gallon', 'gal', 'gallons']:
            return 256.0 * amount/stdAmt
        else:
            print "we can't easily convert from " + unit + " to " + stdUnit
            return 1
    elif stdUnit == 'cup':
        if unit in ['tsp', 'teaspoon', 'teaspoons']:
            return (amount / stdAmt) / 48
        elif unit in ['tbsp', 'tbs', 'tablespoon', 'tablespoons']:
            return (amount / stdAmt) / 16
        elif unit in ['pinch', 'dash']: return 0.00001
        elif unit in ['c', 'cup', 'cups']:
            return amount/stdAmt
        elif unit in ['pint', 'pt', 'pints']:
            return 2.0 * amount/stdAmt
        elif unit in ['quart', 'quarts', 'qt']:
            return 4.0 * amount/stdAmt
        elif unit in ['gallon', 'gal', 'gallons']:
            return 8.0 * amount/stdAmt
        else:
            print "we can't easily convert from " + unit + " to " + stdUnit
            return 1
    elif stdUnit == 'ounce':
        if unit in ['lb', 'lbs', 'pound', 'pounds']:
            return 16.0 * amount / stdAmt
        elif unit in ['kg', 'kilo', 'kilos', 'kilograms']:
            return 35.274 * amount / stdAmt
        elif unit in ['g', 'gs', 'grams']:
            return 0.35 * amount / stdAmt
        elif unit in ['oz', 'ozs', 'ounces']:
            return amount/stdAmt
        else:
            print "we can't easily convert from " + unit + " to " + stdUnit
            return 1
    elif stdUnit == 'pound':
        if unit in ['lb', 'lbs', 'pound', 'pounds']:
            return amount / stdAmt
        elif unit in ['kg', 'kilo', 'kilos', 'kilograms']:
            return 2.2 * amount / stdAmt
        elif unit in ['g', 'gs', 'grams']:
            return 0.0035 * amount / stdAmt
        elif unit in ['oz', 'ozs', 'ounces']:
            return (amount/stdAmt) / 16
        else:
            print "we can't easily convert from " + unit + " to " + stdUnit
            return 1
    elif stdUnit == 'kilogram':
        if unit in ['lb', 'lbs', 'pound', 'pounds']:
            return (amount / stdAmt) / 2.2
        elif unit in ['kg', 'kilo', 'kilos', 'kilograms']:
            return amount / stdAmt
        elif unit in ['g', 'gs', 'grams']:
            return (amount / stdAmt) / 1000
        elif unit in ['oz', 'ozs', 'ounces']:
            return 0.028 * amount / stdAmt
        else:
            print "we can't easily convert from " + unit + " to " + stdUnit
            return 1
    elif stdUnit == 'gram':
        if unit in ['lb', 'lbs', 'pound', 'pounds']:
            return 454 * amount / stdAmt
        elif unit in ['kg', 'kilo', 'kilos', 'kilograms']:
            return 1000 * amount / stdAmt
        elif unit in ['g', 'gs', 'grams']:
            return amount / stdAmt
        elif unit in ['oz', 'ozs', 'ounces']:
            return 28.35 * amount / stdAmt
        else:
            print "we can't easily convert from " + unit + " to " + stdUnit
            return 1
