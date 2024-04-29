import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_file(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)


def list_all_videos(videos):
    print("-"*50)
    for index,video in enumerate(videos,start=1):
        print(f"{index}. Video name: {video['name']}, Duration: {video['time']}")
    print("-"*50)

def add_video(videos):
    name = input("Enter the video name: ")
    time = input("Enter the video time: ")
    videos.append({'name':name,'time':time})
    save_file(videos)


def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number you want to update: "))
    if 1<=index<=len(videos):
        name = input("Enter the video name: ")
        time = input("Enter the video time: ")
        videos[index-1]= {'name':name,'time':time}
        save_file(videos)
        print(f"Video no. {index} Updated")
    else:
        print("Invalid option selected")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number you want to delete: "))
    if 1<=index<=len(videos):
        # videos.pop(index-1)
        del videos[index-1]
        save_file(videos)
        print(f"Video no. {index} Deleted")
    else:
        print("Invalid option selected")


def main():
    videos = load_data()
    while True:
        print("\n ---------------YOUTUBE MANAGER-----------------")
        print("1. List All Videos")
        print("2. Add a Video")
        print("3. Update a Video")
        print("4. Delete a Video")
        print("5. Exit from the App")
        print('-'*60)
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                print("Thank you for using the app")
                break
            case _:
                print("Invalid choice")
    
if __name__ == "__main__":
    main()
        

