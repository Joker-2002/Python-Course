import requests

def fetch_info():
    
    url = "https://api.freeapi.app/api/v1/public/books/39"
    response = requests.get(url)
    info = response.json()

    if info['success'] and 'data' in info:
        data = info['data']
        print("--------Inforamation On Book------")
        print(f"Title: {data['volumeInfo']['title']}")
        print(f"Author: {data['volumeInfo']['authors'][0]}")
        print(f"Published on: {data['volumeInfo']['publishedDate']} and Published By: {data['volumeInfo']['publisher']}")
        print(f"Description: {data['volumeInfo']['description']}")
    else:
        raise Exception("Error in fetching data")
    
def main():
    try: 
        fetch_info()
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
