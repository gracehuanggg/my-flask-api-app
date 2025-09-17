from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to My Flask API App!</h1><p>Available endpoints:</p><ul><li>/random-meal - Get a random meal recipe</li></ul>"

@app.route("/random-meal")
def random_meal():
    try:
        response = requests.get("https://www.themealdb.com/api/json/v1/1/random.php", timeout=10)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()
        meal = data ["meals"][0]
        result = {
            "name": meal["strMeal"],
            "category": meal["strCategory"],
            "cuisine": meal ["strArea"],
            "instructions": meal["strInstructions"],
            "image": meal["strMealThumb"]
        }
       
        return jsonify(result)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to fetch random meal: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

