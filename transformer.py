import CookingTerms
from ingredientMatcher import *

def veggify(ingredients, recipe, originalFlavor, IngredientsDict):

    vegetarian = True
    for i in ingredients.keys():
        if "meat" in IngredientsDict[i].superTypes:
            vegetarian = False
            break

    if vegetarian == True:
        print "this is vegetarian and we're going to add some meat!"
        cat = "vegProtein"
    else: # it is not vegetarian
        print "let's make this meaty dish vegetarian"
        cat = "meat"
        
    toSwap = []
    newIng = dict(ingredients)
    newRecipe = recipe
    for i in ingredients.keys():
        if cat in IngredientsDict[i].superTypes:
            toSwap.append(i)
    if len(toSwap) == 0:
        print "this appears to be a vegetarian recipe that does not have any vegetarian protein in it... it's hard to just... add meat.  But feel free to throw some chicken in or something!"
    else:
        for i in toSwap:
            newIng, newRecipe = swapOut(newIng, newRecipe, originalFlavor, IngredientsDict, i)

    return [newIng, newRecipe]

def changeStyle(ingredients, recipe, originalFlavor, IngredientsDict, swapSpice):
    spices = gatherSpices(ingredients, IngredientsDict)
    spiceFlavors = calculateFlavorScore(spices)
    newRecipe = recipe
    newIngredients = dict(ingredients)
    for i in spices:
        newSpice = findBestMatch(i, swapSpice)
        newWeight = weightFactor(newSpice, ingredients[i]["weight"], i, IngredientsDict)
        newIngredients = swapIngredients(newIngredients, i, newSpice, newWeight)
        newRecipe = swapInRecipe(newRecipe, i, newSpice)
    return [newIngredients, newRecipe]

def gatherSpices(ingredients, dicto):
    spices = []
    for i in ingredients:
        ### how to access ingredient dictionary
        if i in dicto["Herbs"].subTypes or i in dictor["Spices"].subTypes:
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
    return ingredients

def swapOut(ingredients, recipe, originalFlavor, IngreDict, swap=""):
    if swap == "":
        swap = raw_input("did you have an ingredient in mind? if so, please type it here.")
        while swap not in ingredients.keys() or swap != "":
            swap = raw_input("I didn't see that in my ingredients; please try again, lower case, or hit enter if you just want me to pick.")
    target = raw_input("did you want to switch it with anything in particular?")
    while target not in IngreDict.keys() or target != "":
        target = raw_input("I don't know how to use that ingredient... either try again, lower case, or hit enter if you trust me")
    if swap == "":
        swap = findSwap(ingredients)
    if target == "":
        targetOptions = collectSubTypes(IngredientsDict["Ingredients"])
        target = findBestMatch(swap, targetOptions)
    targetWeighted = weightFactor(target, ingredients[swap]["weight"], swap, IngreDict)
    newIngredients = swapIngredients(ingredients, swap, target, targetWeighted)
    newRecipe = swapInRecipe(newRecipe, swap, target)
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
        return "EuroFlavors"
    elif spices == "arab":
        return "ArabFlavors"
    elif spices == "south asian":
        return "SouthAsianFlavors"
    elif spices == "east asian":
        return "EastAsianFlavors"

def swapIngredients(ingredients, old, new, newWeight):
    newIng = removeKey(ingredients, old)
    newIng[new] = newWeight
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
