# THIS IS A DOG API

import requests

def fetch_dog():
    url1 = "https://api.freeapi.app/api/v1/public/dogs?page=1&limit=10&query=Affenpinscher"
    url2 = "https://api.freeapi.app/api/v1/public/dogs/124"
    url3 = "https://api.freeapi.app/api/v1/public/dogs/dog/random"
    
    response1 = requests.get(url1)
    response2 = requests.get(url2)
    response3 = requests.get(url3)

    dog1 = response1.json()
    dog2 = response2.json()
    dog3 = response3.json()

    if dog1['success'] and dog2['success'] and dog3['success']:
        print("----------INFORMATION ON DOGS-------")

        data1 = dog1['data'] 
        print(f"1. Name of Breed: {data1['data'][0]['name']}")
        print(f"\t Breed for: {data1['data'][0]['bred_for']} ")
        print(f"\t Life Span: {data1['data'][0]['life_span']}")
        print(f"\t Temperament: {data1['data'][0]['temperament']}")
        print(f"\t Origin: {data1['data'][0]['origin']}")
        print(f"\t Image: {data1['data'][0]['image']['url']}")
        
        
        data2 = dog2['data'] 
        print(f"2. Name of Breed: {data2['name']}")
        print(f"\t Breed for: {data2['bred_for']}")
        print(f"\t Life Span: {data2['life_span']}")
        print(f"\t Temperament: {data2['temperament']}")
        # print(f"\t Origin: {data2['data'][0]['origin']}")
        print(f"\t Image: {data2['image']['url']}")
        

        data3 = dog3['data'] 
        print(f"3. Name of Breed: {data3['name']}")
        print(f"\t Breed for: {data3['breed_group']}")
        print(f"\t Life Span: {data3['life_span']}")
        print(f"\t Temperament: {data3['temperament']}")
        # print(f"\t Origin: {data3['data'][0]['origin']}")
        print(f"\t Image: {data3['image']['url']}")

    else:
        raise Exception("Failed to Fetch User Data!!")


def main():
    try: 
        fetch_dog()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()