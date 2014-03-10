from CookingTerms import collectIngredients # or whatever it is called
from parse import *
from transformer import *
from ingredientMatcher import *
from sets import Set
import pprint

def SwapRecipes():

    measures = Set(['tsp', 'teaspoon', 'teaspoons', 'tbsp', 'tbs', 'tablespoon', 'tablespoons',
                    'pinch', 'dash', 'lb', 'lbs', 'pound', 'pounds', 'kg', 'kilo',
                    'kilos', 'kilograms', 'g', 'gs', 'grams', 'oz', 'ozs', "ounce", 'ounces',
                    'c', 'cup', 'cups', 'pint', 'pt', 'pints', 'quart', 'quarts', 'qt',
                    'gal', 'gallon', 'gallons'])

    print "so you'd like to mix up a recipe, eh? \n \n \n"

    IngreDict, implements, methods = collectIngredients()
    
    ingredInput = raw_input("Please give me the ingredients:")
    ingredients = processIngredients(ingredInput, IngreDict, measures)
    
    recipeInput = raw_input("Please give me the sequence of operations")
    recipe = recipeInput
    #recipe = processRecipe(ingredients, steps) # NOT DONE YET

    print "you can do four sorts of transformations: making it vegetarian (or non-vegetarian, if it is vegetarian); change the style of cuisine; scale the recipe up or down; or swap a particular ingredient"
    transformation = raw_input("please say 'veg', 'style', 'scale', or 'swap' respectively for these options")
    while transformation != "veg" and transformation != "style" and transformation != "scale" and transformation != "swap":
        transformation = raw_input("please say 'veg', 'style', 'scale', or 'swap' respectively for these options")

    originalFlavor = calculateFlavorScore(ingredients, IngreDict)
    spiceType = "Spices"

    if transformation == "veg":
        newIng, newRecipe = veggify(ingredients, recipe, originalFlavor, IngreDict) 
    elif transformation == "style":
        newType = raw_input("what flavor palate do you want: you can choose European, Arab, South Asian, or East Asian")
        while newType != 'european' and newType != 'arab' and newType != 'south asian' and newType != 'east asian':
            newType = raw_input("sorry, try again: what spice palate do you want? please type, in lower case, european, arab, south asian, or east asian.")
        spiceType = typeConverter(newType)
        newIng, newRecipe = changeStyle(ingredients, recipe, originalFlavor, IngreDict, spiceType)
    elif transformation == "scale":
        newIng = scaleRecipe(ingredients)
        newRecipe = recipe
    elif transformation == "swap":
        newIng, newRecipe = swapOut(ingredients, recipe, originalFlavor, IngreDict)

    # we should maybe not even do this next line:
    #newRecipe, newIngredients = balanceOut(newRecipe, newIngredients, originalFlavor, IngreDict, spiceType)

    # we need something to print the recipe...
    print "here are your new ingredients"
    pprint.pprint(newIng)
    print "and your recipe is "
    print newRecipe

    return
