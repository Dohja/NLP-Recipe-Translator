from CookingTerms import collectIngredients() # or whatever it is called
from ingredientMatcher import *

def SwapRecipes():    

    print "so you'd like to mix up a recipe, eh? \n \n \n"

    IngreDict = collectIngredients() # or whatever it is called
    
    ingredInput = raw_input("Please give me the ingredients:")
    ingredients = processIngredients(ingredInput, IngreDict) # OBV NOT DONE YET; ingredients SHOULD BE A DICTIONARY where the KEY is the INGREDIENT OBJECT and the VAL is the WEIGHT

    recipeInput = raw_input("Please give me the sequence of operations")
    recipe = processRecipe(ingredients, steps) # OBV NOT DONE YET

    print "you can do four sorts of transformations: making it vegetarian (or non-vegetarian, if it is vegetarian); change the style of cuisine; scale the recipe up or down; or swap a particular ingredient"
    transformation = raw_input("please say 'veg', 'style', 'scale', or 'swap' respectively for these options")

    originalFlavor = calculateFlavorScore(ingredients)

    if transformation == "veg":
        newIng, newRecipe = veggify(ingredients, recipe, originalFlavor, IngreDict) ## IMPLEMENT
    elif transformation == "style":
        newIng, newRecipe = changeStyle(ingredients, recipe, originalFlavor, IngreDict)
    elif transformation == "scale":
        newIng = scaleRecipe(ingredients)
        newRecipe = recipe.copy ## what does this look like
    elif transformation == "swap":
        newIng, newRecipe = swapOut(ingredients, recipe, originalFlavor, IngreDict)

    newRecipe, newIngredients = balanceOut(newRecipe, newIngredients, originalFlavor, IngreDict, spiceType) # NOT DONE YET

return

def removeKey(d, key):
    r = dict(d)
    del r[key]
    return r
