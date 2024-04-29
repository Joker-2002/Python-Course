import requests

def fetch_meal():
    url = "https://gist.githubusercontent.com/tsalb/dd0576209bb960051375698ee4a665cc/raw/4e7ca072015a1cef77cc97006814999be184d597/meal-response.json"
    reponse = requests.get(url)
    info = reponse.json()

    if 'meals' in info:
        meal = info['meals']
        print("--------------Meal List------------")
        for i in range(0,24):
            print(f"{i+1}. Meal Name: {meal[i]['strMeal']}")
            print(f"\t Origin: {meal[i]['strArea']}")
            print(f"\t Ingredients")
            for j in range(1,14):
                if meal[i][f'strIngredient{j}']  != "":
                    print(f"\t\t {j}. {meal[i][f'strIngredient{j}']} ({meal[i][f'strMeasure{j}']})")
            print(f"\t Instruction to cook: {meal[i]['strInstructions']}")
            print(f"\t Youtube Link: {meal[i]['strYoutube']}")
            print("*"*100)
    else:
        raise Exception("Unable to fetch Data")
    
def main():
    try:
        fetch_meal()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
