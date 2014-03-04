import random
import CookingTerms
from math import fabs

def calculateFlavorScore(ingredients):

    score = {"sweet": 0, "salty": 0, "sour": 0, "bitter": 0, "umami": 0, "hot": 0}

    for ing in ingredients:
        for taste in ["sweet", "salty", "sour", "bitter", "umami", "hot"]:
            score[taste] += ing.taste * ingredients[ing]

    return score

def findSwap(ingredients):
    # just take a random ingredient that is important enough?
    trySwap = ""
    cutoff = 3.0
    testList = []

    while len(testList) < 3:
        cutoff -= .333333333333333
        testList = [ing for ing in ingredients.keys() if ingredients[ing] > cutoff]
    trySwap = random.choice(testList)

    return trySwap

def weightFactor(newIngredient, origWeight, swap, IngredientDict):
    toMatch = {"sweet": IngredientDict[swap]["sweet"]*origWeight,
               "salty": IngredientDict[swap]["salty"]*origWeight,
               "sour": IngredientDict[swap]["sour"]*origWeight,
               "bitter": IngredientDict[swap]["bitter"]*origWeight,
               "umami": IngredientDict[swap]["umami"]*origWeight,
               "hot": IngredientDict[swap]["hot"]*origWeight}

    weightFactor = 0.0
    for i in ["sweet", "salty", "sour", "bitter", "umami", "hot"]:
        weightFactor += IngredientDict[newIngredient][i]
    return weightFactor / 6.0
    
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

# need to make all possible subsets that are similar ENOUGH to consider

def calculateFlavorDiff(originalFlavor, newFlavor):
    flavorDiff = Ingredient("flavorDiff")
    for i in ["sweet", "salty", "sour", "bitter", "umami", "hot"]:
        taste = originalFlavor.i - newFlavor.i
        flavorDiff.setTaste(i, taste)
    return flavorDiff

def collectSubTypes(ingredient):
    if ingredient.subTypes == []: return [ingredient]
    else:
        sub = []
        for i in ingredient.subTypes:
            sub.extend(collectSubTypes(i))
        return sub

def gatherOptions(difference, HnS, options, counter):
    for k in options.keys():
        localDiff = calculateFlavorDiffer(difference, calculateFlavorScore(options[k]))
        for i in HnS:
            strongest = findStrongestTaste(i) 
            maxRatio = localDiff.strongest/i.strongest
            for r in range(maxRatio):
                options[counter] = dict(options[k])
                options[counter][i] = r
                counter += 1
    return options

def findBestOption(options, flavorDiff):
    bestOption = None
    bestScore = 100000000
    for option in options:
        score = 0
        diff = calculateFlavorDiff(flavorDiff, option)
        for i in ["sweet", "salty", "sour", "bitter", "umami", "hot"]:
            score += math.fabs(diff[i])
        if score < bestScore:
            bestScore = score
            bestOption = option
    return bestOption
    
def findStrongestTaste(ingredient):
    strongest = None
    valence = 0
    for i in ["sweet", "salty", "sour", "bitter", "umami", "hot"]:
        if ingredient[i] > valence:
            strongest = i
    return strongest
