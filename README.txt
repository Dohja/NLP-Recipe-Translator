David Ryan, Joe BLass & Ted Wu
Natural Language Processing Final Project
README

Language used: python 2.7

Our method uses modules "random", "math", "nltk", "fractions", "bs4" (AKA Beautiful Soup), 
"urllib2", "sets", "pprint", and of course "json".  All of these can be found using pip
(and many should be preinstalled, such as random and math and sets).

Main method: in userInterface.py: SwapRecipes(url), where url is the address of 
an AllRecipes.com recipe.  You will be prompted for the transformation, etc., that 
you want.  Make sure you use all lower case when interacting with the program.

Please note that our program will have tremendous difficulty swapping out something that
is not in our master ingredient list. If it breaks doing this, or fails to swap accurately, 
that is the cause.  Either try an ingredient we have instantiated (or an alternate recipe), or ]
contact us and we will add the ingredient to our master list.
