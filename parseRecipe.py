from bs4 import BeautifulSoup
import urllib2
	
def parseHTML(url):
	usock = urllib2.urlopen(url)
	HTML = usock.read()
	soup = BeautifulSoup(HTML)
	name = soup.find(id="itemTitle").string
	servings = soup.find(id="zoneIngredients")['data-currentservings']
	ingredients = soup.find_all("ul", {"class" : "ingredient-wrap"})
	
	ingredientList = []
	
	for ingredient in ingredients:
		ing = ingredient.find_all("p", {"class" : "fl-ing"})
		for i in ing:
			ingName = i.find("span", {"class":"ingredient-name"})
			name = ingName.string
			ingAmt = i.find("span", {"class":"ingredient-amount"})
			if ingAmt == None:
				amt = 'to taste'
				name = name.replace(', to taste', '')
				name = name.replace(' to taste','')
			else:
				amt = ingAmt.string
			ingredientList.append(amt+' '+name)
	print 'Ingredients: '
	print ingredientList
	print '\n'
	
	directions = ''
	dir = soup.find('div', {'class' : 'directions'})
	dir = dir.find('ol')
	dir = dir.find_all('li')
	for d in dir:
		directions += '\n'+d.string
	print "Directions: "	
	print directions
	print '\n'
	return ingredientList, directions
