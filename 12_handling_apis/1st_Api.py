import requests

def fetch_user_info():
    url = "https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"
    response = requests.get(url)
    info = response.json()

    if info['success'] and 'data' in info:
        data1 = info['data']
        # data2 = data1['data'][0]['name']
        # for key,value in data2.items():
        #     print(f"{key} and {value}")
        # print(f"My name is {data2['title']} {data2['first']} {data2['last']}")
        data2 = data1['data']
        print("THIS IS A FORM.")
        print("-"*100)
        for i in data2:
            print(f"Name: {i['name']['first']} {i['name']['last']} ")
            print(f"Gender: {i['gender']}")
            print(f"DOB: {i['dob']['date']} and Age: {i['dob']['age']}")
            print(f"Address: {i['location']['street']['number']} {i['location']['street']['number']}, City: {i['location']['city']}, State: {i['location']['state']}")
            print(f"Country: {i['location']['country']}, Pin-code: {i['location']['postcode']}")
            print("-"*100)
    else:
        raise Exception("Failed to Fetch User Data!!")
    

def main():
    try:
        fetch_user_info()
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()





