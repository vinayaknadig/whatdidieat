import json
import requests
import urllib.parse, urllib.request
import ssl

context = ssl._create_unverified_context()


# Edamam Food Database API Developer Keys
app_key  = "2b275be2a3c02179a2d034ee7c4a4477"
app_id   = "971b8291"

base_parse_url     = "https://api.edamam.com/api/food-database/parser?"
base_nutrients_url = "https://api.edamam.com/api/food-database/nutrients"

# url-encoder for Parser GET request
def buildParserURL(food_item):
    params = {"ingr"   :food_item,
              "app_id" :app_id,
              "app_key":app_key          
         }
    return base_parse_url + urllib.parse.urlencode(params)

# url-encoder for Nutrients POST request
def buildNutrientsParams(food_id, measureURI):
    ingredients = [{ 
                   "quantity": 1, 
                   "measureURI": measureURI, 
                   "foodId": food_id
                  }]
    print("ingredients",json.dumps(ingredients))
    params = {
              "yield" : 1,
              "ingredients" : ingredients
             }
    
    return json.dumps(params)

# Parser GET Response
def getParserResults(url):
    try:
        response = urllib.request.urlopen(url, context = context)
        return json.load(response)
    finally:
        if response != None:
            response.close()

# Nutrients POST Response

def getNutrientResponse(url, parameters):
    try:
        response = requests.post(url, headers = {'Content-Type': 'application/json'},data = parameters)
        print(response)
        return response.json()
    finally:
        return

# Id parser from GET Response
def getResultIds(results):
    for r in results:
        print(r)
    return [(results["hints"][0]["food"]["foodId"],results["hints"][0]["measures"][0]["uri"])]


def getNutrients(foods):
    nutrition_list = []
    for f in foods:
        print("this is f", f)
        params = buildNutrientsParams(f[0],f[1])
        print("params",params)
        nutrients = getNutrientResponse(base_nutrients_url,params)
        print(nutrients)
        nutrition_list.append(nutrients)
    return nutrition_list

# url = buildParserURL("burger")
# print("url", url)
# results = getParserResults(url)
# print("results", results)
# ids = getResultIds(results)
# print("ids", ids)
# getNutrients(ids)

params = {
    'ingredients' : {
                    'quantity' : 1,
                    'measureURI' : 'http://www.edamam.com/ontologies/edamam.owl#Measure_gram',
                    'foodId'    : 'food_bgm7topbhq6exua24ls9ea468fyd'
    }
}
def func1():
    try:
        response = requests.post("https://api.edamam.com/api/food-database/nutrients", Headers = {"Content-Type" : "application/json"}, data = params, params = {'app_id' : app_id, 'app_key' : app_key})
        return response.json()
    finally:
        return
a = func1()
print(a)