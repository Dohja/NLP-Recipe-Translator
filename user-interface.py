from CookingTerms import collectIngredients() # or whatever it is called
from ingredientMatcher import *

def SwapRecipes():    

    print "so you'd like to mix up a recipe, eh? \n \n \n"

    IngreDict = collectIngredients() # or whatever it is called
    
    ingredInput = raw_input("Please give me the ingredients:")
    ingredients = processIngredients(ingredInput, IngreDict) # OBV NOT DONE YET; ingredients SHOULD BE A DICTIONARY where the KEY is the INGREDIENT OBJECT and the VAL is the WEIGHT

    recipeInput = raw_input("Please give me the sequence of operations")
    recipe = processRecipe(ingredients, steps) # OBV NOT DONE YET

    swap = raw_input("did you have an ingredient in mind? if so, please type it here")
    while swap not in ingredients.keys() or swap != "":
        swap = raw_input("I didn't see that in my ingredients; please try again, lower case, or hit enter if you just want me to pick something")

    target = raw_input("did you want to switch it with anything in particular?")
    while target not in IngredientList or swap != "":
        target = raw_input("I don't know how to use that ingredient... either try again, lower case, or hit enter if you trust me")

    if swap == "":
        swap = findSwap(ingredients)

    originalFlavor = calculateFlavorScore(ingredients) 
    # flavorScore and flavorNoSwap are going to be of type Ingredient, and their internal scores will determine how we're doing

    newIngredients = removeKey(ingredients, swap)
    newRecipe = removeSwap(recipe, swap) # NOT DONE YET what does this even look like?  Unclear yet
    
    if target != "":
        targetWeighted = weightFactor(target, ingredients, swap, IngreDict)
        newIngredients[target] = targetWeighted

    flavorNoSwap = calculateFlavorScore(newIngredients)

    # whether we've added something or not, now we need to balance the recipe

    newRecipe, newIngredients = balanceOut(newRecipe, newIngredients, originalFlavor) # NOT DONE YET

     
    
    

return

def removeKey(d, key):
    r = dict(d)
    del r[key]
    return r

def balanceOut(newRecipe, newIngredients, oldRecipe, oldIngredients):
    # add things to newRecipe until it matches oldRecipe


    return [newRecipe, newIngredients]
