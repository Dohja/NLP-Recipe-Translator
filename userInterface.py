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
                    'gal', 'gallon', 'gallons', 'to taste', 'cloves'])

    print "so you'd like to mix up a recipe, eh? \n \n \n"
    IngreDict, implements, methods, assocTools = collectIngredients()
    ingredInput, recipeInput = parseHTML(url)
    ingredients = processIngredients(ingredInput, IngreDict, measures)

    recipe = recipeInput.lower()

    meths = [x for x in methods if x in recipe]
    impls = [x for x in implements if x in recipe]
    for method, tool in assocTools.iteritems():
	    if method in meths and tool not in impls:
		    impls.append(tool)
    impls = list(set(impls)) #hack to eliminate duplicates
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
        newIng, newRecipe = swapOut(ingredients, recipe, originalFlavor, IngreDict, 'swap')

    # we need something to print the recipe...
    print
    print "--------------------------------------"
    print "\nhere are your new ingredients:\n"
    printIngredients(newIng)
    print "\nand your recipe is:"
    print newRecipe
    print "\nHere are the primary cooking methods for this recipe: " + str(meths)
    print "Here are the implements: " + str(impls)
    ingredientList = [newIng[ing] for ing in newIng]

    response = []
    for key, row in ingredients.iteritems():
        if row['name']==None:
            print 'ERROR: NO NAME'
            return -1
        if row['quantity'] ==None:
            row['quantity']= 1.0
        if row['measurement'] == None:
            row['measurement']='units'
        if row['description']== None or row['description']== '':
            row['description'] = 'none'
        if row['preparation']==None or row['preparation']== '':
            row['preparation']='none'
        response.append({'name':row['name'], 'quantity':row['quantity'], 
		'measurement':row['measurement'], 'descriptor':row['description'], 
		'preparation':row['preparation']})
    output = json.dumps(response)
    print '\n\n\n'    
    
    return output

def printIngredients(ings):
    for ing in ings:
        if ings[ing]['quantity'] == None: q = ''
        else: q = str(ings[ing]['quantity']) + " "
        if ings[ing]['measurement'] == None: m = ''
        else: m = ings[ing]['measurement'] + " "
        if ings[ing]['description'] == None: d = ''
        else: d = ings[ing]['description'] + " "
        if ings[ing]['preparation'] == None: p = ''
        else: p = ", " + ings[ing]['preparation']
        print q + m + d + ings[ing]['name'] + p
    return



# ================== EXAMPLE RECIPES ================== #

#SwapRecipes('http://allrecipes.com/Recipe/Braised-Balsamic-Chicken/Detail.aspx?event8=1&prop24=SR_Thumb&e11=braised%20balsamic%20chicken&e8=Quick%20Search&event10=1&e7=Recipe&soid=sr_results_p1i1')
#SwapRecipes('http://allrecipes.com/Recipe/Tofu-Parmigiana/Detail.aspx?event8=1&prop24=SR_Thumb&e11=tofu&e8=Quick%20Search&event10=1&soid=sr_results_p1i1')
#SwapRecipes('http://allrecipes.com/Recipe/Chicken-Cordon-Bleu-II/Detail.aspx?soid=recs_recipe_8')
#SwapRecipes('http://allrecipes.com/Recipe/Venison-Bacon-Burgers/Detail.aspx?soid=recs_recipe_9')
#SwapRecipes('http://allrecipes.com/Recipe/Irish-Cream-Chocolate-Cheesecake/Detail.aspx?soid=photos_vote_5')
#SwapRecipes('http://allrecipes.com/Recipe/Chicken-Breasts-with-Balsamic-Vinegar-and-Garlic/Detail.aspx?soid=carousel_0_rotd&prop24=rotd')
#SwapRecipes('http://allrecipes.com/Recipe/Amazingly-Easy-Irish-Soda-Bread/Detail.aspx?soid=recs_recipe_4')
#SwapRecipes('http://allrecipes.com/Recipe/Cajun-Chicken-Pasta-2/Detail.aspx?soid=recs_recipe_3')
#SwapRecipes('http://allrecipes.com/recipe/bacon-cheeseburgers/')
#SwapRecipes('http://allrecipes.com/Recipe/Strawberry-Spinach-Salad-I/Detail.aspx')
#SwapRecipes('http://allrecipes.com/Recipe/Mediterranean-Pasta/Detail.aspx?event8=1&prop24=SR_Title&e11=pasta&e8=Quick%20Search&event10=1&e7=Home%20Page&soid=sr_results_p1i5')

