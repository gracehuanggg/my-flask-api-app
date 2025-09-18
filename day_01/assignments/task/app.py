from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# First route as home page
@app.route("/")
def home():
    return "<h1>Welcome to My Flask API App!" \
    "</h1><p>Available endpoints:</p><ul>" \
    "<li>/random-meal - Get a random meal recipe</li>" \
    "<li>/search-meal?name=Arrabiata - Search for a meal by name </li>"\
    "<li>/search-by-letter?letter=a- Search meals by first letter </li>" \
    "</ul>"

#Second route gets the random meal
@app.route("/random-meal")
def random_meals():
    limit = requests.args.get("limit", 5)
    limit = int(limit)
    meals = data ["meals"][0]
    for i in range (limit):
        url = "https://www.themealdb.com/api/json/v1/1/random.php"
        response = requests.get(url)
        data = response.json()
        meals.append = {
            "name": meal["strMeal"],
                "category": meal["strCategory"],
                "cuisine": meal ["strArea"],
                "instructions": meal["strInstructions"],
                "image": meal["strMealThumb"]
        }   
    return jsonify(result)
    

# Third Route Utilizes Query Parameter for limit of number of random meals 
@app.route ("/search-meal")
def search_meal():
    meal_name = requests.arg.get("name", "")

    if meal_name == "":
        return jsonify ({"error": "Please include a meal name like ?=Arrabiata"})
    url=f"https://www.themealdb.com/api/json/v1/1/search.php?s={meal_name}"
    response = requests.get(url)
    data = response.json

    if not data ["meals"]:
        return jsonify({"message": f"No meals found starting with '{letter}'"})
    
    meals = []
    for meal in data ["meals"]:
        meals.append({
            "name": meal["strMeal"],
            "category": meal["strCategory"],
            "cuisine": meal ["strArea"],
            "instructions": meal["strInstructions"],
            "image": meal["strMealThumb"]
        })
    return jsonify({"meals": meals})

# Third Route implements query parameters
@app.route("/search-by-letter")
def search_by_letter():
    letter = requests.arg.get("letter", "")

    if letter == "":
        return jsonify ({"error":"Please include a letter like letter = g"})
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?f={letter}"
    response = requests.get(url)
    data = response.json()

    if not data ["meals"]:
        return jsonify({"message": f"No meals found starting with '{letter}'"})
    
    meals = []
    for meal in data ["meals"]:
        meals.append({
            "name": meal["strMeal"],
            "category": meal["strCategory"],
            "cuisine": meal ["strArea"],
            "instructions": meal["strInstructions"],
            "image": meal["strMealThumb"]
        })
    return jsonify({"meals": meals})

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)