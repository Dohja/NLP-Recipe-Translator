class Ingredient():
    def __init__(self, name):
        self.name = name
        self.subTypes = []
        self.superTypes = []
        self.sweet = None
        self.sour = None
        self.bitter = None
        self.salty = None
        self.umami = None
        self.hot = None # hot meaning spicy
        self.units = None # is this a measured ingredient or a counted ingredient?

    def addSubType(self, group):
        self.subTypes.extend(group)
        for i in group:
            if self not in i.superTypes:
                i.addSuperType(self)

    def addSuperType(self, parent):
        self.superTypes.append(parent)
        if self not in parent.subTypes:
            parent.subTypes.append(self)

    def setTaste(self, taste, rating):
        self.taste = rating
        # so, setTaste(umami, 4); setTaste(sour, 5) or such to define each ingredient

    def setUnits(self, units):
        if units == "weight": self.units = "weight"
        elif units == "volume": self.units = "volume"
        elif units == "count": self.units = "count"
        else:
            unit = raw_input("Please indicate whether " + self.name + " is measured by weight, volume, or count")
            self.setUnits(unit)

    def printSubTypes(self):
        if self.subTypes == []: print self.name
        else:
            print self.name
            for i in self.subTypes:
                i.printSubTypes()

## Here comes the heirarchy
Ingredients = Ingredient("Ingredients")

#ingredient super types
Protein = Ingredient("protein")
Plants = Ingredient("plants") # done
Spices = Ingredient("spices")
Dairy = Ingredient("dairy")
CookingMedia = Ingredient("cooking Media")

# Types of plant ingredients
Veg = Ingredient("veg") # done
Herbs = Ingredient("herbs") # done
Grain = Ingredient("grain") # done
Fruit = Ingredient("fruit") # Done
Nuts = Ingredient("nuts") # done

# Types of protein
Meat = Ingredient("meat")
VegProtein = Ingredient("veg Protein")
Seafood = Ingredient("seafood")
Poultry = Ingredient("poultry")

# types of spices
EuroSpices = Ingredient("European Spices") # done
EastAsianSpices = Ingredient("East Asian Spices")
SouthAsianSpices = Ingredient("South Asian Spices") # done
ArabSpices = Ingredient("Arab Spices") # done

# types of cooking media
Oils = Ingredient("oils")
Broth = Ingredient("broth")
Stock = Ingredient("stock")
Wine = Ingredient("wine")

# types of meat
Beef = Ingredient("beef")
Pork = Ingredient("pork")
Lamb = Ingredient("lamb")

# types of beef
BeefRibs = Ingredient("beef ribs")
Steak = Ingredient("steak")
RibTips = Ingredient("rib tips")
BeefStew = Ingredient("beef stew")
VealCutlet = Ingredient("veal cutlet")

# types of pork
PorkRibs = Ingredient("pork ribs")
PorkChops = Ingredient("pork chops")
PorkRoast = Ingredient("pork roast")
PorkCutlet = Ingredient("pork cutlets")

# types of lamb
LambChops = Ingredient("lamb chops")
Leg = Ingredient("leg of lamb")
LambRoast = Ingredient("lamb roast")

# types of veg protein
Tofu = Ingredient("Tofu")
Seitan = Ingredient("Seitan")
Tempeh = Ingredient("Tempeh")

# Types of seafood
Molluscs = Ingredient("molluscs")
Crustaceans = Ingredient("crustaceans")
Fish = Ingredient("fish")

BlueFish = Ingredient("blue fish")
Salmon = Ingredient("salmon")
WhiteFish = Ingredient("whitefish")
Catfish = Ingredient("catfish")
Cod = Ingredient("cod")
Eel = Ingredient("eel")
Haddock = Ingredient("haddock")
Halibut = Ingredient("halibut")
Mackerel = Ingredient("mackerel")
Pike = Ingredient("pike")
Pollock = Ingredient("pollock")
Skate = Ingredient("skate")
Snapper = Ingredient("snapper")
Sole = Ingredient("sole")
Swordfish = Ingredient("swordfish")
Tilapia = Ingredient("tilapia")
Trout = Ingredient("trout")
Tuna = Ingredient("tuna")

Crab = Ingredient("crab")
Lobster = Ingredient("lobster")
Shrimp = Ingredient("shrimp")

Clam = Ingredient("clam")
Mussel = Ingredient("mussel")
Octopus = Ingredient("octopus")
Oyster = Ingredient("oyster")
Scallop = Ingredient("scallop")
Squid = Ingredient("squid")

# Types of poultry
Chicken = Ingredient("chicken")
Duck = Ingredient("duck")
Goose = Ingredient("goose")
Eggs = Ingredient("eggs")
Pigeon = Ingredient("pigeon")
Quail = Ingredient("quail")
Turkey = Ingredient("turkey")

# kinds of vegetable
Artichokes = Ingredient("artichokes")
Asparagus = Ingredient("asparagus")
Avocado = Ingredient("avocado")
GreenBeans = Ingredient("green beans")
BlackBeans = Ingredient("black beans")
PintoBeans = Ingredient("pinto beans")
Beets = Ingredient("beets")
Broccoli = Ingredient("broccoli")
BrusselsSprouts = Ingredient("brussels sprouts")
Cabbage = Ingredient("cabbage")
Cauliflower = Ingredient("cauliflower")
CollardGreens = Ingredient("collard greens")
Cucumber = Ingredient("cucumber")
BellPepper = Ingredient("bell pepper")
BananaPepper = Ingredient("banana pepper")
Carrots = Ingredient("carrots")
Celery = Ingredient("celery")
Corn = Ingredient("corn") # should also be a grain
Eggplant = Ingredient("eggplant")
Fennel = Ingredient("fennel")
Garlic = Ingredient("garlic") # should also be an herb
Ginger = Ingredient("ginger") # should also be a spice
Horseradish = Ingredient("horseradish") # should also be an herb
Kale = Ingredient("kale")
Leeks = Ingredient("leeks")
Lentils = Ingredient("lentils")
Lettuce = Ingredient("lettuce")
OysterMushrooms = Ingredient("oyster mushrooms")
ButtonMushrooms = Ingredient("button mushrooms")
ShiitakeMushrooms = Ingredient("shiitake mushrooms")
CriminiMushrooms = Ingredient("crimini mushrooms")
ChanterelleMushrooms = Ingredient("chanterelle mushrooms")
PortabelloMushrooms = Ingredient("portabello mushrooms")
PorciniMushrooms = Ingredient("porcini mushrooms")
MorelMushrooms = Ingredient("morel mushrooms")
Okra = Ingredient("okra")
Onions = Ingredient("onions")
Peas = Ingredient("peas")
Radishes = Ingredient("radishes")
Shallots = Ingredient("shallots")
Spinach = Ingredient("spinach")
AcornSquash = Ingredient("acorn squash")
ButternutSquash = Ingredient("butternut squash")
SpaghettiSquash = Ingredient("spaghetti squash")
Tomatoes = Ingredient("tomatoes")
GreenTomatoes = Ingredient("green tomatoes")
Tomatillos = Ingredient("tomatillos")
Turnips = Ingredient("turnips")
Zucchini = Ingredient("zucchini")
Potatoes = Ingredient("potatoes")
SweetPotatoes = Ingredient("sweet potatoes")

# kinds of herbs
Parsley = Ingredient("parsley")
CurleyParsley = Ingredient("curley parsley")
FlatParsley = Ingredient("flat parsley")
Parsley.addSubType([CurleyParsley, FlatParsley])

Cilantro = Ingredient("cilantro")
Basil = Ingredient("basil")
Watercress = Ingredient("watercress")
Dill = Ingredient("dill")
Mint = Ingredient("mint")
BayLeaves = Ingredient("bay leaves")
Rosemary = Ingredient("rosemary")
Lavender = Ingredient("lavender")
Thyme = Ingredient("thyme")
Chives = Ingredient("chives")
Sorrel = Ingredient("sorrel")

# kinds of spices
# European
AllSpice = Ingredient("allspice")
Anise = Ingredient("anise")
Mustard = Ingredient("mustard")
Cayenne = Ingredient("cayenne") # should be in east and south asian too
Cinnamon = Ingredient("cinnamon") # should be in all
FennelSeed = Ingredient("fennel seed")
BlackPepper = Ingredient("black pepper") # all
Salt = Ingredient("salt") #all
Sugar = Ingredient("sugar") #all
BrownSugar = Ingredient("brown sugar") # all
Mace = Ingredient("mace") # south asian too
Nutmeg = Ingredient("nutmeg")
Paprika = Ingredient("paprika") # south asian, arab
Saffron = Ingredient("saffron") # all
Tarragon = Ingredient("tarragon") # arab
Turmeric = Ingredient("turmeric") # south asian, arab
Sage = Ingredient("sage")

# East Asian

# South Asian
CaromSeeds = Ingredient("carom seeds")
Asafoetida = Ingredient("asafoetida")
Cardamom = Ingredient("cardamom")
Cumin = Ingredient("cumin") # should be in arab too
Curry = Ingredient("curry")
Coriander = Ingredient("coriander")
ChiliPepper = Ingredient("chili pepper")
Fenugreek = Ingredient("fenugreek")
KaffirLime = Ingredient("kaffir lime")
Lemongrass = Ingredient("lemongrass")

# Arab
Cardamom = Ingredient("cardamom")
Baharat = Ingredient("baharat")
Sumac = Ingredient("sumac")
Zatar = Ingredient("zatar")

# Grains
Wheat = Ingredient("wheat")
Rice = Ingredient("rice")
Quinoa = Ingredient("quinoa")
Millet = Ingredient("millet")
Teff = Ingredient("teff")
Flour = Ingredient("flour")
Buckwheat = Ingredient("buckwheat")
Barley = Ingredient("barley")
Bulghur = Ingredient("bulghur")

WhiteFlour = Ingredient("white flour")
WholeWheatFlour = Ingredient("whole wheat flour")
BuckwheatFlour = Ingredient("buckwheat flour")
CousCous = Ingredient("couscous")
CornFlour = Ingredient("corn flour")

WhiteRice = Ingredient("white rice")
JasmineRice = Ingredient("jasmine rice")
BrownRice = Ingredient("brown rice")
BasmatiRice = Ingredient("basmati rice")
SushiRice = Ingredient("sushi rice")
WildRice = Ingredient("wild rice")

# Fruit
Apple = Ingredient("apple")
Banana = Ingredient("banana")
Pear = Ingredient("pear")
Grapes = Ingredient("grapes")
Mango = Ingredient("mango")
Peach = Ingredient("peach")
Berries = Ingredient("berries")
Lemon = Ingredient("lemon")
Lime = Ingredient("lime")
Orange = Ingredient("orange")
Grapefruit = Ingredient("grapefruit")
Apricots = Ingredient("apricots")
Fig = Ingredient("fig")
Pineapple = Ingredient("pineapple")
Melon = Ingredient("melon")
Nectarines = Ingredient("nectarines")

Strawberries = Ingredient("strawberries")
Raspberries = Ingredient("raspberries")
Blueberries = Ingredient("blueberries")
Blackberries = Ingredient("blackberries")

Watermelon = Ingredient("watermelon")
Honeydew = Ingredient("honeydew")
Cantaloupe = Ingredient("cantaloupe")

# Nuts
Almonds = Ingredient("almonds")
Cashews = Ingredient("cashews")
Peanuts = Ingredient("peanuts")
Pistachios = Ingredient("pistachios")
Hazelnuts = Ingredient("hazelnuts")
Walnuts = Ingredient("walnuts")
Pecans = Ingredient("pecans")
Chestnuts = Ingredient("chestnuts")
PineNuts = Ingredient("pine nuts")
Macadamia = Ingredient("macadamia nuts")

# Oils
PeanutOil = Ingredient("peanut oil")
OliveOil = Ingredient("olive oil")
SafflowerOil = Ingredient("safflower oil")
CanolaOil = Ingredient("canola oil")
VegetableOil = Ingredient("vegetable oil")
WalnutOil = Ingredient("walnut oil")
SesameOil = Ingredient("sesame oil")

# Broth
ChickenBoullion = Ingredient("chicken boullion")
ChickenBroth = Ingredient("chicken broth")
BeefBoullion = Ingredient("beef boullion")
BeefBroth = Ingredient("beef broth")
VegetableBoullion = Ingredient("vegetable boullion")
VegetableBroth = Ingredient("vegetable broth")
FishBoullion = Ingredient("fish boullion")
FishBroth = Ingredient("fish broth")

# Stock
ChickenStock = Ingredient("chicken stock")
BeefStock = Ingredient("beef stock")
VegetableStock = Ingredient("vegetable stock")
FishStock = Ingredient("fish stock")
LobsterStock = Ingredient("lobster stock")

# Wine
RedWine = Ingredient("red wine")
WhiteWine = Ingredient("white wine")

Cabernet = Ingredient("cabernet")
Beaujolais = Ingredient("beaujolais")
Malbec = Ingredient("malbec")
Merlot = Ingredient("merlot")
PinotNoir = Ingredient("pinot noir")
Syrah = Ingredient("syrah")
Shiraz = Ingredient("shiraz")
Zinfandel = Ingredient("zinfandel")

Chardonnay = Ingredient("chardonnay")
Muscat = Ingredient("muscat")
PinotBlanc = Ingredient("pinot blanc")
PinotGrigio = Ingredient("pinot grigio")
Riesling = Ingredient("riesling")
Sauvignon = Ingredient("sauvignon")

# Dairy
Milk = Ingredient("milk")
Cream = Ingredient("cream")
Cheese = Ingredient("cheese")
Butter = Ingredient("butter")
Ghee = Ingredient("ghee")
Yogurt = Ingredient("yogurt")

GreekYogurt = Ingredient("greek yogurt")
PlainYogurt = Ingredient("plain yogurt")
FlavoredYogurt = Ingredient("flavored yogurt")
Kefir = Ingredient("kefir")

BlueCheese = Ingredient("blue cheese")
GoatCheese = Ingredient("goat cheese")
Cheddar = Ingredient("cheddar")
Mozzarella = Ingredient("mozarella")
Swiss = Ingredient("swiss cheese")
Parmesan = Ingredient("parmesan")
Asiago = Ingredient("asiago")
Gorgonzola = Ingredient("gorgonzola")
CreamCheese = Ingredient("cream cheese")

# putting together heirarchy

# PROTEIN #######################################################

Beef.addSubType([BeefRibs, Steak, RibTips, BeefStew, VealCutlet])

Pork.addSubType([PorkRibs, PorkChops, PorkRoast, PorkCutlet])

Lamb.addSubType([LambChops, Leg, LambRoast])

Meat.addSubType([Beef, Pork, Lamb])

VegProtein.addSubType([Tofu, Seitan, Tempeh])

Molluscs.addSubType([Clam, Mussel, Octopus, Oyster, Scallop, Squid])

Crustaceans.addSubType([Crab, Lobster, Shrimp])

Fish.addSubType([BlueFish, Salmon, WhiteFish, Catfish, Cod, Eel, Haddock, Halibut, Mackerel, Pike,
                 Pollock, Skate, Snapper, Sole, Swordfish, Tilapia, Trout, Tuna])

Seafood.addSubType([Molluscs, Crustaceans, Fish])

Poultry.addSubType([Chicken, Duck, Goose, Eggs, Pigeon, Quail, Turkey])

Protein.addSubType([Meat, VegProtein, Seafood, Poultry])

# PLANTS ######################################
Veg.addSubType([Artichokes, Asparagus, GreenBeans, Beets, Broccoli, BrusselsSprouts, Cabbage, CollardGreens, BellPepper,
                BananaPepper, Carrots, Celery, Corn, Eggplant, Garlic, Ginger, Horseradish, Kale, Leeks, Lettuce, OysterMushrooms,
                ButtonMushrooms, ShiitakeMushrooms, CriminiMushrooms, ChanterelleMushrooms, PortabelloMushrooms, PorciniMushrooms,
                MorelMushrooms, Okra, Onions, Peas, Radishes, Shallots, Spinach, AcornSquash, ButternutSquash, SpaghettiSquash,
                Tomatoes, GreenTomatoes, Tomatillos, Turnips, Zucchini, Fennel, Avocado, Cauliflower, Cucumber, Potatoes,
                SweetPotatoes, Lentils, BlackBeans, PintoBeans])

Herbs.addSubType([Parsley, Cilantro, Basil, Watercress, Dill, Mint, BayLeaves,
                  Rosemary, Lavender, Thyme, Chives, Sorrel, Garlic, Horseradish])

Rice.addSubType([WhiteRice, JasmineRice, BrownRice, BasmatiRice, SushiRice, WildRice])
Flour.addSubType([WhiteFlour, WholeWheatFlour, BuckwheatFlour, CousCous, CornFlour])
Grain.addSubType([Wheat, Rice, Quinoa, Millet, Teff, Flour, Buckwheat, Barley, Bulghur])

Berries.addSubType([Strawberries, Raspberries, Blueberries, Blackberries])
Melon.addSubType([Watermelon, Honeydew, Cantaloupe])
Fruit.addSubType([Apple, Banana, Pear, Grapes, Mango, Peach, Berries, Lemon, Lime, Orange,
                  Grapefruit, Apricots, Fig, Pineapple, Melon, Nectarines])

Nuts.addSubType([Almonds, Cashews, Peanuts, Pistachios, Hazelnuts, Walnuts, Pecans, Chestnuts, PineNuts, Macadamia])

Plants.addSubType([Veg, Herbs, Fruit, Grain, Nuts])

# SPICES ########################################################
ArabSpices.addSubType([Cumin, Cinnamon, Cayenne, BlackPepper, Salt, Sugar, BrownSugar, Paprika, Saffron, Tarragon,
                       Turmeric, Cardamom, Baharat, Sumac, Zatar])
SouthAsianSpices.addSubType([Cayenne, Cinnamon, BlackPepper, Ginger, Salt, Sugar, BrownSugar, Mace, Paprika, Saffron,
                             Turmeric, CaromSeeds, Asafoetida, Cardamom, Cumin, Curry, Coriander, ChiliPepper,
                             Fenugreek, KaffirLime, Lemongrass])
EuroSpices.addSubType([AllSpice, Anise, Mustard, Cayenne, Cinnamon, FennelSeed, BlackPepper, BlackPepper, Salt,
                       Sugar, BrownSugar, Mace, Nutmeg, Paprika, Paprika, Saffron, Tarragon, Turmeric, Sage, Ginger])

Spices.addSubType([EuroSpices, EastAsianSpices, SouthAsianSpices, ArabSpices]) # not done with EastAsia; done with others?

# DAIRY #################################################################
Cheese.addSubType([BlueCheese, GoatCheese, Cheddar, Mozzarella, Swiss, Parmesan, Asiago, Gorgonzola, CreamCheese])
Yogurt.addSubType([GreekYogurt, PlainYogurt, FlavoredYogurt])
Dairy.addSubType([Milk, Cream, Cheese, Butter, Ghee, Yogurt])

# COOKING MEDIA ######################################################
Oils.addSubType([PeanutOil, OliveOil, SafflowerOil, CanolaOil, VegetableOil, WalnutOil, SesameOil])

Broth.addSubType([ChickenBoullion, ChickenBroth, BeefBoullion, BeefBroth, VegetableBoullion, VegetableBroth, FishBoullion, FishBroth])

Stock.addSubType([ChickenStock, BeefStock, VegetableStock, FishStock, LobsterStock])

RedWine.addSubType([Cabernet, Beaujolais, Malbec, Merlot, PinotNoir, Syrah, Shiraz, Zinfandel])
WhiteWine.addSubType([Chardonnay, Muscat, PinotBlanc, PinotGrigio, Riesling, Sauvignon])
Wine.addSubType([RedWine, WhiteWine])

CookingMedia.addSubType([Oils, Broth, Stock, Wine, Butter, Ghee])
###########################################

Ingredients.addSubType([Protein, Plants, Spices, Dairy, CookingMedia])
