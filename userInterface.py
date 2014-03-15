from CookingTerms import *
from parse import *
from transformer import *
from ingredientMatcher import *
from parseRecipe import *
from sets import Set
import pprint
import json

def SwapRecipes(url):

    measures = Set(['tsp', 'teaspoon', 'teaspoons', 'tbsp', 'tbs', 'tablespoon', 'tablespoons',
                    'pinch', 'dash', 'lb', 'lbs', 'pound', 'pounds', 'kg', 'kilo',
                    'kilos', 'kilograms', 'g', 'gs', 'grams', 'oz', 'ozs', "ounce", 'ounces',
                    'c', 'cup', 'cups', 'pint', 'pt', 'pints', 'quart', 'quarts', 'qt',
                    'gal', 'gallon', 'gallons', 'to taste'])

    print "so you'd like to mix up a recipe, eh? \n \n \n"
    IngreDict, implements, methods, assocTools = collectIngredients()
    ingredInput = parseHTML(url)[0]
    ingredients = processIngredients(ingredInput, IngreDict, measures)
    ingredList, recipeInput = parseHTML(url)

    recipe = recipeInput.lower()

    meths = [x for x in methods if x in recipe]
    impls = [x for x in implements if x in recipe]
    for method, tool in assocTools.iteritems():
	    if method in meths:
		    impls.append(tool)
    print "you can do four sorts of transformations: making it vegetarian (or non-vegetarian, if it is vegetarian); change the style of cuisine; scale the recipe up or down; or swap a particular ingredient"
    transformation = raw_input("please say 'veg', 'style', 'scale', or 'swap' respectively for these options: ")
    while transformation != "veg" and transformation != "style" and transformation != "scale" and transformation != "swap":
        transformation = raw_input("please say 'veg', 'style', 'scale', or 'swap' respectively for these options: ")

    originalFlavor = calculateFlavorScore(ingredients, IngreDict)
    spiceType = "Spices"

    if transformation == "veg":
        newIng, newRecipe = veggify(ingredients, recipe, originalFlavor, IngreDict) 
    elif transformation == "style":
        newType = raw_input("what flavor palate do you want: you can choose European, Arab, South Asian, or East Asian: ")
        while newType != 'european' and newType != 'arab' and newType != 'south asian' and newType != 'east asian':
            newType = raw_input("sorry, try again: what spice palate do you want? please type, in lower case, european, arab, south asian, or east asian: ")
        spiceType = typeConverter(newType)
        newIng, newRecipe = changeStyle(ingredients, recipe, originalFlavor, IngreDict, spiceType)
    elif transformation == "scale":
        newIng = scaleRecipe(ingredients)
        newRecipe = recipe
    elif transformation == "swap":
        newIng, newRecipe = swapOut(ingredients, recipe, originalFlavor, IngreDict)

    # we need something to print the recipe...
    print "here are your new ingredients"
    pprint.pprint(newIng)
    print "and your recipe is "
    print newRecipe
    print "Here are the primary cooking methods for this recipe" + str(meths)
    print "Here are the implements" + str(impls)
    ingredientList = [newIng[ing] for ing in newIng]

    output = json.dumps({"ingredients": ingredientList, "cooking method": meths, "cooking tools": impls})

    return output

SwapRecipes('http://allrecipes.com/Recipe/Paella/Detail.aspx?event8=1&prop24=SR_Thumb&e11=paella&e8=Quick%20Search&event10=1&soid=sr_results_p1i1')
