import requests

base_url = "http://127.0.0.1:5000"

def get_one_rand_meal():
    url=f"{base_url}/api/meal"
    response = requests.get(url)
    print("GET", url)
    print("Status:", response.status_code)
    print("Response JSON:", response.json())
    print("-------------------")

def get_three_rand_meals():
    url=base_url+"api/meals/3"
    response=requests.get(url)
    print("GET", url)
    print("Status:", response.status_code)
    print("Response JSON:", response.json())
    print("-------------------")

if __name__ == "__main__":
    get_one_rand_meal
    get_three_rand_meals
