import nltk
import fractions
from CookingTerms import Ingredient

def processIngredients(ingList, ingDict, measures):
    ingredients = {}
    for ingredient in ingList:
	    ingredients = processOneIngredient(ingredient, ingDict, ingredients, measures)
    return ingredients

def processOneIngredient(ing, ingDict, allIng, measures):
    solution = {}
    tokens = nltk.PunktWordTokenizer().tokenize(ing)
    if tokens == []: return allIng
    else:
        num, units = extractQM(tokens, ingDict, measures)
        desc, name, prep = extractIngredient(tokens, ingDict, units, num)
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
        if quantity == None and isNumber(words[i]): # only initialize the first number to quantity
            quantity = convertToNum(words[i])
        if isNumber(words[i]) and words[i+1] in measures: # UNLESS there is a measure after. This avoids putting a number in "prep" as the quantity
            quantity = convertToNum(words[i])
            measurement = words[i+1]
            break

            ### this allows us to account for parentheticals, such that 1 (4.5 ounce) can mushrooms
            ### outputs 4.5 ounce as its amount and unit, and can becomes part of the description
            ### it will also cut off the program after 1 tbsp but not the above
        
    return [quantity, measurement]

def isNumber(string):
    try:
        float(string)
        return True
    except ValueError:
        try:
            float(string[0])
            return True
        except ValueError:
            return False

def convertToNum(fraction):
	if "/" not in fraction:
		return float(fraction)
	frac = fraction.split("/")
	answer = 0
	if " " in frac[0]:
		mixed = frac[0].split()
		answer = float(mixed[0])
		answer += float(mixed[1]) / float(frac[1])
	else:
		answer += float(frac[0]) / float(frac[1])
	return answer

def extractIngredient(tokens, ingDict, units, num):
    descriptor = None
    prep = None
    if units != None:
        tokens = tokens[tokens.index(units) + 1:]
        if tokens[0] == ')': tokens = tokens[1:]
    elif num != None:
        for i in tokens:
            check = convertToNum(i)
            if check == num:
                index = tokens.index(i)
                break
        tokens = tokens[index+ 1:]
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
    if name in ingDict.keys():
        std = ingDict[name].stdMeasure.split()
        stdAmt = convertToNum(std[0])
        stdU = " ".join(std[1:])
        if stdU == unit: return amount/stdAmt
        else: return convertWeight(amount, unit, stdAmt, stdU)
    else:
        new = Ingredient(name, ingDict)
        return 1

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
        elif unit in ['oz', 'ozs', "ounce", 'ounces']:
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
        elif unit in ['oz', 'ozs', "ounce", 'ounces']:
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
        elif unit in ['oz', 'ozs', "ounce", 'ounces']:
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
        elif unit in ['oz', 'ozs', "ounce", 'ounces']:
            return 28.35 * amount / stdAmt
        else:
            print "we can't easily convert from " + unit + " to " + stdUnit
            return 1
    else: return 1
