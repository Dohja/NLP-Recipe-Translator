import CookingTerms
from ingredient-matcher import *

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
    newRecipe = recipe.copy ### WHAT DOES THIS LOOK LIKE
    for i in ingredients.keys():
        if cat in IngredientsDict[i].superTypes:
            toSwap.append(i)
    if len(toSwap) == 0:
        ### only possible if vegetarian without any vegProtein, i.e., just veggies
        newIng, newRecipe = addMeat(ingredients, recipe, IngredientsDict) ### MAKE THIS
    else:
        for i in toSwap:
            newIng, newRecipe = swapOut(newIng, newRecipe, originalFlavor, IngredientsDict, i)

    return [newIng, newRecipe]

def changeStyle(ingredients, recipe, originalFlavor, IngredientsDict):
    spices = gatherSpices(ingredients)
    spiceFlavors = calculateFlavorScore(spices)
    newRecipe = recipe.copy ### WHAT DOES THIS LOOK LIKE
    newIngredients = dict(ingredients)
    newType = raw_input("what spice palate do you want: you can choose European, Arab, South Asian, or East Asian")
    while newType != 'european' or newType != 'arab' or newType != 'south asian' or newType != 'east asian':
        newType = raw_input("sorry, try again: what spice palate do you want? please type, in lower case, european, arab, south asian, or east asian.")
    swapSpice = typeConverter(newType)
    newSpices = collectSubTypes(IngredientsDict[swapSpice])
    for i in spices:
        newSpice = findBestMatch(i, newSpices)
        newWeight = weightFactor(newSpice, ingredients[i], i, IngredientsDict)
        newIngredients = swapIngredients(newIngredients, i, newSpice, newWeight)
        newRecipe = swapInRecipe(newRecipe, i, newSpice)
    return [newIngredients, newRecipe]

def scaleRecipe(ingredients):
    ## NOTE: THIS DOES NOT ACCOUNT FOR FOODSTUFFS THAT SCALE DIFFERENTLY, I.E., SALT
    ## ALSO DOES NOT ACCOUNT FOR SCALED COOKING TIME
    print "what would you like to scale by a factor of?"
    scale = raw_input("1 leaves the recipe unchanged; 0.5 would halve it; 2 would double it; etc")
    scale = float(scale)
    for i in ingredients.keys():
        ingredients[i] *= scale
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
    targetWeighted = weightFactor(target, ingredients[swap], swap, IngreDict)
    newIngredients = swapIngredients(ingredients, swap, target, targetWeighted)
    newRecipe = swapInRecipe(newRecipe, swap, target)
    return [newIngredients, newRecipe]

def balanceOut(recipe, ingredients, originalFlavor, IngreDict, spices = "all"):
    
    newFlavor = calculateFlavorScore(ingredients)
    flavorDiff = calculateFlavorDiff(originalFlavor, newFlavor)

    if spices == "all":
        spices = "Spices"
    elif spices == "european":
        spices = "EuroSpices"
    elif spices == "arab":
        spices = "ArabSpices"
    elif spices == "south asian":
        spices = "SouthAsianSpices"
    elif spices == "east asian":
        spices = "EastAsianSpices"

    herbsAndSpices = collectSubTypes(spices)
    herbsAndSpices.extend(collectSubTypes(herbs))

    options = gatherOptions(flavorDiff, herbsAndSpices, {0: {}}, 1)
    bestOption = findBestOption(options, flavorDiff)
    recipe.addToRecipe(bestOption) ####
    for ing in bestOption:
        ingredients[ing] = bestOption[ing]
    return [recipe, ingredients]

def typeConverter(spices):
    if spices == "all":
        return "Spices"
    elif spices == "european":
        return "EuroSpices"
    elif spices == "arab":
        return "ArabSpices"
    elif spices == "south asian":
        return "SouthAsianSpices"
    elif spices == "east asian":
        return "EastAsianSpices"

def swapIngredients(ingredients, old, new, newWeight):
    newIng = removeKey(ingredients, old)
    newIng[new] = newWeight
    return newIng

def swapInRecipe(recipe, old, new):
    ## replaces all instances of old with new in a recipe
    return newRecipe

def addMeat(ing, recipe, ingDict):
    ### add meat to a vegetarian recipe
    return [newIng, newRecipe]
