import random
import CookingTerms
from math import fabs

def calculateFlavorScore(ingredients, ingreDict):

    score = {"sweet": 0, "salty": 0, "sour": 0, "bitter": 0, "umami": 0, "hot": 0}

    for ing in ingredients:
        score["sweet"] += ingreDict[ing].sweet * ingredients[ing]["weight"]
        score["salty"] += ingreDict[ing].salty * ingredients[ing]["weight"]
        score["sour"] += ingreDict[ing].sour * ingredients[ing]["weight"]
        score["bitter"] += ingreDict[ing].bitter * ingredients[ing]["weight"]
        score["umami"] += ingreDict[ing].umami * ingredients[ing]["weight"]
        score["hot"] += ingreDict[ing].hot * ingredients[ing]["weight"]

    return score

def findSwap(ingredients):
    # just take a random ingredient that is important enough?
    trySwap = ""
    cutoff = 3.0
    testList = []

    while len(testList) < 3:
        cutoff -= .333333333333333
        testList = [ing for ing in ingredients.keys() if ingredients[ing]["weight"] > cutoff]
    trySwap = random.choice(testList)

    return trySwap

def weightFactor(newIngredient, origWeight, swap, IngredientDict):
    toMatch = {"sweet": IngredientDict[swap].sweet*origWeight,
               "salty": IngredientDict[swap].salty*origWeight,
               "sour": IngredientDict[swap].sour*origWeight,
               "bitter": IngredientDict[swap].bitter*origWeight,
               "umami": IngredientDict[swap].umami*origWeight,
               "hot": IngredientDict[swap].hot*origWeight}

    weightFactor = 0.0
    for i in ["sweet", "salty", "sour", "bitter", "umami", "hot"]:
        weightFactor += IngredientDict[swap].i / IngredientDict[newIngredient].i
    return weightFactor / 6.0

def findBestMatch(ing, replacements):
    bestMatch = None
    bestScore = 1000000000
    for i in replacements:
        score = 0
        diff = calculateFlavorDiff(ing, i)
        for t in ["sweet", "salty", "sour", "bitter", "umami", "hot"]:
            score += math.fabs(diff[i])
        if score < bestScore:
            bestScore = score
            bestMatch = i
    return bestMatch

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
