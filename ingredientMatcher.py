import random
from CookingTerms import *
from math import fabs

def calculateFlavorScore(ingredients, ingreDict):

    score = {"sweet": 0, "salty": 0, "sour": 0, "bitter": 0, "umami": 0, "hot": 0}

    for ing in ingredients:
        if ingreDict[ing].sweet == None: continue
        else:
            score["sweet"] += ingreDict[ing].sweet * ingredients[ing]["weight"]
            score["salty"] += ingreDict[ing].salty * ingredients[ing]["weight"]
            score["sour"] += ingreDict[ing].sour * ingredients[ing]["weight"]
            score["bitter"] += ingreDict[ing].bitter * ingredients[ing]["weight"]
            score["umami"] += ingreDict[ing].umami * ingredients[ing]["weight"]
            score["hot"] += ingreDict[ing].hot * ingredients[ing]["weight"]

    return score

def findSwap(ingredients, IngreDict):
    # just take a random ingredient that is important enough?
    trySwap = ""
    cutoff = 3.0
    testList = []
    while len(testList) < 3:
        cutoff -= .333333333333333
        testList = [ing for ing in ingredients.keys() if ingredients[ing]["weight"] > cutoff]
    trySwap = random.choice(testList)
    return IngreDict[trySwap]

def weightFactor(newIngredient, origWeight, swap, IngredientDict):
    toMatch = {"sweet": IngredientDict[swap].sweet*origWeight,
               "salty": IngredientDict[swap].salty*origWeight,
               "sour": IngredientDict[swap].sour*origWeight,
               "bitter": IngredientDict[swap].bitter*origWeight,
               "umami": IngredientDict[swap].umami*origWeight,
               "hot": IngredientDict[swap].hot*origWeight}

    weightFactor = 0.0
    weightFactor += IngredientDict[swap].sweet / IngredientDict[newIngredient].sweet
    weightFactor += IngredientDict[swap].salty / IngredientDict[newIngredient].salty
    weightFactor += IngredientDict[swap].sour / IngredientDict[newIngredient].sour
    weightFactor += IngredientDict[swap].bitter / IngredientDict[newIngredient].bitter
    weightFactor += IngredientDict[swap].umami / IngredientDict[newIngredient].umami
    weightFactor += IngredientDict[swap].hot / IngredientDict[newIngredient].hot
    return weightFactor / 6.0

def findBestMatch(ing, replacements, replaceWithSelf=False):
    bestMatch = None
    bestScore = 1000000000
    for i in replacements:
        if i.sweet == None: continue
        if i == ing and replaceWithSelf == False: continue
        else:
            score = 0
            diff = calculateFlavorDiff(ing, i)
            score += fabs(diff.sweet)
            score += fabs(diff.salty)
            score += fabs(diff.sour)
            score += fabs(diff.umami)
            score += fabs(diff.bitter)
            score += fabs(diff.hot)
            if score < bestScore:
                bestScore = score
                bestMatch = i
    return bestMatch

def calculateFlavorDiff(originalFlavor, newFlavor):
    flavorDiff = Ingredient("flavorDiff", {})
    flavorDiff.setTaste("sweet", originalFlavor.sweet - newFlavor.sweet)
    flavorDiff.setTaste("salty", originalFlavor.salty - newFlavor.salty)
    flavorDiff.setTaste("sour", originalFlavor.sour - newFlavor.sour)
    flavorDiff.setTaste("bitter", originalFlavor.bitter - newFlavor.bitter)
    flavorDiff.setTaste("umami", originalFlavor.umami - newFlavor.umami)
    flavorDiff.setTaste("hot", originalFlavor.hot - newFlavor.hot)
    return flavorDiff

def collectSubTypes(ingredient):
    sub = [ingredient]
    for i in ingredient.subTypes:
        sub.extend(collectSubTypes(i))
    return sub
