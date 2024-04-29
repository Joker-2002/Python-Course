import requests

def fetch_meal():
    url = "https://api.freeapi.app/api/v1/public/meals/1"
    reponse = requests.get(url)
    info = reponse.json()
    
    if info['success'] and 'data' in info:
        print({info['message']})
        data = info['data']
        print(f"Meal Name: {data['strMeal']}")
        print(f"Category: {data['strCategory']} , Type of Meal: {data['strArea']}")

        print("---Ingredients Required:--- ")
        for i in range(1,17):
            print(f"\t{i}. {data[f'strIngredient{i}']} ({data[f'strMeasure{i}']})")
        
        print(f"Instructions: {data['strInstructions']}")
        print(f"Meal Image: {data['strMealThumb']}")
        print(f"Youtube Link: {data['strYoutube']}")

    else:
        print("Error")  

def main():
    try:
        fetch_meal()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()