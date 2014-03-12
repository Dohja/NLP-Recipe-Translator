from bs4 import BeautifulSoup
import urllib2
	
def parseHTML(url):
	usock = urllib2.urlopen(url)
	HTML = usock.read()
	soup = BeautifulSoup(HTML)
	name = soup.find(id="itemTitle").string
	servings = soup.find(id="zoneIngredients")['data-currentservings']
	print 'servings: '+str(servings)
	
	ingredients = soup.find_all("ul", {"class" : "ingredient-wrap"})
	
	ingredientList = {}
	
	for ingredient in ingredients:
		ing = ingredient.find_all("p", {"class" : "fl-ing"})
		for i in ing:
			ingName = i.find("span", {"class":"ingredient-name"})
			name = ingName.string
			ingAmt = i.find("span", {"class":"ingredient-amount"})
			if ingAmt == None:
				print 'NOAMT: '
				amt = 'to taste'
				name = name.replace(', to taste', '')
				name = name.replace(' to taste','')
			else:
				amt = ingAmt.string
			ingredientList[name] = amt
	print ingredientList
	print '\n\n'
	
	directionList = []
	dir = soup.find('div', {'class' : 'directions'})
	dir = dir.find('ol')
	dir = dir.find_all('li')
	for d in dir:
		directionList.append(d.string)
	print directionList
	print '\n\n'
	return ingredientList, directionList
	
def newProcessIngredients(ingredientList):
	ingredients = {}
	for ingredient, measure in ingredientList.iteritems():
		num, units = newExtractQM(measure)
		
		tokens = nltk.PunktWordTokenizer().tokenize(ingredient)
		
def newExtractQM(measure, ingDict, measureSet):
	quantity = None
	measurement = None
	index=0
	words = measure.split()
	for i in range(len(words)):
		print i
		if words[i] in measureSet:
			measurement = i
			break
		elif i in ingDict:
			measurement = None
			for y in range(0, i):
				
			break
			

	
