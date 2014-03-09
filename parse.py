import nltk
import fractions

def processIngredients(ingText, ingDict, measures):
    ingredients = {}
    ### ingredients will come in looking something like:
        ##"""1 tablespoon soy sauce
        ##2 tablespoons vegetable oil
        ##1 tablespoon Worcestershire sauce
        ##1 teaspoon lemon juice
        ##2 tablespoons brown sugar
        ##2 tablespoons ketchup
        ##6 pork chops, trimmed"""
    ingList = ingText.split('\n')
    for ingredient in ingList:
        ingredients = processOneIngredient(ingredient, ingDict, ingredients, measures)
    return ingredients

def processOneIngredient(ing, ingDict, allIng, measures):
    tokens = nltk.PunktWordTokenizer().tokenize(ing)
    if tokens == []: return allIng
    if tokens[1] == '(':
        closeParen = tokens.index(')')# for parenthetical measures, which we prefer over the count measure
        tokens = tokens[2:closeParen] + tokens[closeParen + 1:] # just remove the parens and the things immediately around them
        # 1 (15 ounce) can artichoke hearts therefore becomes simply 15 ounce artichoke hearts
    number = float(fractions.Fraction(tokens[0])) # float-enize everything, including fractions such as 2/3
    units = "count" # default; if it's not a measure, it's a count
    if tokens[1] in measures:
        units = tokens[1]
    preparation = "" # default: no prep
    if ',' in tokens:
        index = tokens.index(',')
        preparation = " ".join(tokens[i] for i in range(index + 1, len(tokens)))
    else: index = len(tokens)-1

    if units == "count": startAt = 1
    else: startAt = 2
    descriptor, name = extractIngredient(tokens[startAt:index], ingDict)

    weight = calculateWeight(name, ingDict, number, units)

    allIng[name] = {"name": name,
                    "weight": weight,
                    "quantity": number,
                    "measurement": units,
                    "descriptor": descriptor,
                    "preparation": preparation}
    return allIng

def extractIngredient(tokens, ingDict):
    descriptor = ""
    name = ""
    for i in range(len(tokens)):
        descriptor = " ".join(tokens[:i])
        name = " ".join(tokens[i:])
        if name in ingDict.keys(): break
    return [descriptor, name]

def calculateWeight(name, ingDict, amount, unit):
    std = ingDict[name].stdMeasure
    stdU = ingDict[name].units
    if stdU == unit: return amount/std
    else: return convertWeight(amount, unit, std, stdU)

def convertWeight(amount, unit, stdAmt, stdUnit):
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
