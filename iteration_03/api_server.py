from flask import Flask, jsonify
import random

app = Flask(__name__)

#JSON data: List of random meals
random_meal = [
    {
        "name": "Cacio e Pepe", 
        "category": "Pasta",
        "cuisine": "Italian"
     },
     {
        "name":"Chicken Teriyaki",
        "category":"Meat",
        "cuisine":"Japanese"
     },
     {
        "name":"Pad Thai",
        "category":"Noodles",
        "cuisine":"Thai"
     },
     {
         "name":"Shakashuka",
         "category":"Vegeterian",
         "cuisine":"Middle Eastern"
     },
     {
        "name":"Kung Pao Chicken",
        "category":"Meat",
        "cuisine":"Chinese"
     },
     {
        "name":"Dark Chocolate Cake",
        "category":"Dessert",
        "cuisine":"American"
     }
]

#Route 1: Home route
@app.route("/")
def home():
    html_content = """
        <h1>Random Meal API</h1>
        <p> Be sure to visit http://127.0.0.1:5000/api/meal for a random meal </p>
        <p>Be sure to visit http://127.0.0.1:5000/api/meals/3 for 3 funny jokes!</p>
    """
    return html_content

# Route 2: Returns 1 random meal in JSON format
@app.route("/api/meal")
def get_one_rand_meal():
    meal = random.choice(random_meal)
    return jsonify (meal)

# Route 3: Returns N random meals in JSON format
@app.route("/api/meals/<int:n>")
def get_n_rand_meals(n):
    results = []
    for i in range (n):
        meal = random.choice(random_meal)
        results.append(meal)
    return jsonify (results)

if __name__ == "__main__":
    app.run(debug=True)
