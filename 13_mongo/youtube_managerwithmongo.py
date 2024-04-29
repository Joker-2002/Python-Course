import pymongo
from bson import ObjectId

# mongodb+srv://youtubepy:youtubepy@cluster0.ndpbcw9.mongodb.net/?retryWrites=true&w=majority

client = pymongo.MongoClient("mongodb+srv://youtubepy:youtubepy@cluster0.ndpbcw9.mongodb.net/")

db = client["ytmanager"]
video_collection = db["video"]

# print(video_collection)


def list_all_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']} Video name: {video['name']}, Duration: {video['time']}")


def add_video(name,time):
    video_collection.insert_one({'name':name,'time':time})


def update_video(video_id,new_name,new_time):
    video_collection.update_one({'_id':ObjectId(video_id)},{'$set':{'name':new_name,'time':new_time}})


def delete_video(video_id):
    # video_collection.delete_one({'_id':video_id}) #gives error it cannot fetch the _id as it is a object type
    video_collection.delete_one({'_id':ObjectId(video_id)})



def main():
    while True:
        print("-------YOUTUBE MANAGER---------")
        print("1. List All Videos")
        print("2. Add a Video")
        print("3. Update a Video")
        print("4. Delete a Video")
        print("5. Exit from App")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_all_videos()
        
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name,time)
        
        elif choice == '3':
            list_all_videos()
            video_id = input("Enter the video id you want to update: ")
            name = input("Enter the updated video name: ")
            time = input("Enter the updated video time: ")
            update_video(video_id,name,time)
        
        elif choice == '4':
            list_all_videos()
            video_id = input("Enter the video id you want to delete: ")
            delete_video(video_id)
        
        elif choice == '5':
            print("-----------THANK YOU FOR USING THE APP!!---------")
            break
        
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()