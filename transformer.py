from CookingTerms import *
from ingredientMatcher import *

def veggify(ingredients, recipe, originalFlavor, IngredientsDict):

    vegetarian = True
    for i in ingredients.keys():
        if IngredientsDict["meat"] in IngredientsDict[i].superTypes:
            vegetarian = False
            break

    if vegetarian == True:
        print "this is vegetarian and we're going to add some meat!"
        cat = "veg Protein"
    else: # it is not vegetarian
        print "let's make this meaty dish vegetarian"
        cat = "meat"
        
    toSwap = []
    newIng = dict(ingredients)
    newRecipe = recipe
    for i in ingredients.keys():
        if IngredientsDict[cat] in IngredientsDict[i].superTypes:
            toSwap.append(i)
    if len(toSwap) == 0:
        print "this appears to be a vegetarian recipe that does not have any vegetarian protein in it... it's hard to just... add meat.  But feel free to throw some chicken in or something!"
    else:
        for i in toSwap:
            newIng, newRecipe = swapOut(newIng, newRecipe, originalFlavor, IngredientsDict, i, "veg Protein")

    return [newIng, newRecipe]

def changeStyle(ingredients, recipe, originalFlavor, IngredientsDict, swapSpice):
    spices = gatherSpices(ingredients, IngredientsDict)
    spiceList = {}
    for i in spices: spiceList[i] = (ingredients[i])
    print "our spices to swap out are " + str(spices)
    spiceFlavors = calculateFlavorScore(spiceList, IngredientsDict)
    newRecipe = recipe
    newIngredients = dict(ingredients)
    for i in spices:
    #    newSpice = findBestMatch(i, swapSpice)
        newIngredients, newRecipe = swapOut(newIngredients, newRecipe, originalFlavor, IngredientsDict, i, swapSpice)
    #    newWeight = weightFactor(newSpice, ingredients[i]["weight"], i, IngredientsDict)
    #    newIngredients = swapIngredients(newIngredients, i, newSpice, newWeight, IngredientsDict)
    #    newRecipe = swapInRecipe(newRecipe, i, newSpice)
    return [newIngredients, newRecipe]

def gatherSpices(ingredients, dicto):
    allSpices = collectSubTypes(dicto["Flavors"])
    spices = []
    for i in ingredients:
        ### how to access ingredient dictionary
        if dicto[i] in allSpices:
            spices.append(i)
    return spices

def scaleRecipe(ingredients):
    ## NOTE: THIS DOES NOT ACCOUNT FOR FOODSTUFFS THAT SCALE DIFFERENTLY, I.E., SALT
    ## ALSO DOES NOT ACCOUNT FOR SCALED COOKING TIME
    print "what would you like to scale by a factor of?"
    scale = raw_input("1 leaves the recipe unchanged; 0.5 would halve it; 2 would double it; etc")
    scale = float(scale)
    for i in ingredients.keys():
        ingredients[i]["weight"] *= scale
        ingredients[i]["quantity"] *= scale
    return ingredients

def swapOut(ingredients, recipe, originalFlavor, IngreDict, swap = "", fromGroup = "Ingredients"):
    replaceWithSelf = True
    if swap == "":
        replaceWithSelf = False
        swap = raw_input("did you have an ingredient in mind? if so, please type it here. Type 'you pick' to have me pick")
        while swap not in ingredients.keys() and swap != "":
            swap = raw_input("I didn't see that in my ingredients; here's what you can pick from:" + str(ingredients.keys()) + " or if you prefer, type 'you pick' to have me pick.")
    target = raw_input("did you want to switch " + swap + " with anything in particular? type 'you pick' to have me pick")
    while target not in IngreDict.keys() and target != "you pick":
        target = raw_input("I don't know how to use that ingredient... either try again, or type 'you pick' if you trust me")
    if swap == "you pick":
        swap = findSwap(ingredients)
    else: swap = IngreDict[swap]
    if target == "you pick":
        targetOptions = collectSubTypes(IngreDict[fromGroup])
        target = findBestMatch(swap, targetOptions, replaceWithSelf)
    else: target = IngreDict[target]
    targetWeighted = weightFactor(target.name, ingredients[swap.name]["weight"], swap.name, IngreDict)
    newIngredients = swapIngredients(ingredients, swap.name, target.name, targetWeighted, IngreDict)
    newRecipe = swapInRecipe(recipe, swap.name, target.name)
    return [newIngredients, newRecipe]

def balanceOut(recipe, ingredients, originalFlavor, IngreDict, spices):
    ## maybe leave this out entirely?
    newFlavor = calculateFlavorScore(ingredients)
    flavorDiff = calculateFlavorDiff(originalFlavor, newFlavor)

    herbsAndSpices = collectSubTypes(spices)
    herbsAndSpices.extend(collectSubTypes(herbs))

    options = gatherOptions(flavorDiff, herbsAndSpices, {0: {}}, 1) ### to do
    bestOption = findBestOption(options, flavorDiff) ### to do
    recipe.addToRecipe(bestOption) #### STILL TO DO
    for ing in bestOption:
        ingredients[ing] = bestOption[ing]
    return [recipe, ingredients]

def typeConverter(spices):
    if spices == "all":
        return "HerbsAndSpices"
    elif spices == "european":
        return "European Flavors"
    elif spices == "arab":
        return "Arab Flavors"
    elif spices == "south asian":
        return "South Asian Flavors"
    elif spices == "east asian":
        return "East Asian Flavors"

def swapIngredients(ingredients, old, new, newWeight, IngreDict):
    newIng = removeKey(ingredients, old)
    split = IngreDict[new].stdMeasure.split()
    newAmt = newWeight * float(split[0])
    newUnits = " ".join(split[1:])
    newIng[new] = {"name": new,
                   "quantity": newAmt,
                   "measurement": newUnits,
                   "description": None,
                   "preparation": None,
                   "weight": newWeight}
    return newIng

def swapInRecipe(recipe, old, new):
    newRecipe = recipe.replace(old, new)
    return newRecipe

def addToRecipe(ingredientsAndWeights):
    ## this will be a dictionary of ingredients and their weights to be added to the recipe.
    ## this is NOT swapping or replacing, but rather adding something entirely new.
    ## should we even do this? it's only used in balanceOut, which we should maybe not include
    ## ideas?
    return

def removeKey(d, key):
    r = dict(d)
    del r[key]
    return r
