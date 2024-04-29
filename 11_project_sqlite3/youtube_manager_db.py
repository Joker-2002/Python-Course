import sqlite3

conn = sqlite3.connect("youtube_manager.db")

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Videos(
               ID INTEGER PRIMARY KEY,
               NAME TEXT NOT NULL,
               TIME TEXT NOT NULL
    )
''')

def list_all_videos():
    cursor.execute("SELECT * FROM Videos")
    for a in cursor.fetchall():
        print(f"{a[0]}. Video name: {a[1]}, Duration: {a[2]}")


def add_video(new_name,new_time):
    cursor.execute("INSERT INTO Videos (NAME, TIME) VALUES (?, ?)",(new_name,new_time))
    conn.commit()


def update_video(video_id,new_name,new_time):
    cursor.execute("UPDATE Videos SET NAME = ?,TIME = ? WHERE ID = ?",(new_name,new_time,video_id))
    conn.commit()


def delete_video(video_id):
    cursor.execute("DELETE FROM Videos WHERE ID = ?",(video_id,))
    conn.commit()


def main():
    while True:
        print("\n------------------YOUTUBE MANAGER (USING DATABASE)---------------")
        print("1. List All Videos...")
        print("2. Add a Video...")
        print("3. Update a Video...")
        print("4. Delete a Video...")
        print("5. Exit From The App...")
        print("-"*70)
        choice = input("Enter your Choice: ")

        if choice == "1":
            list_all_videos()

        elif choice == "2":
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name,time)

        elif choice == "3":
            list_all_videos()
            video_id = int(input("Enter the video id you want to update: "))
            if video_id in [video[0] for video in cursor.execute("SELECT ID FROM Videos")]:
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                update_video(video_id,name,time)
            else:
                print("You Entered Invalid Video ID")

        elif choice == "4":
            list_all_videos()
            video_id = int(input("Enter the video id you want to delete: "))
            if video_id in [video[0] for video in cursor.execute("SELECT ID FROM Videos")]:
                delete_video(video_id)
            else:
                print("You Entered Invalid Video ID")

        elif choice == "5":
            print("-----THANK YOU FOR USING THE APP-----")
            break

        else:
            print("Invalid Choice")

    conn.close()


if __name__ == "__main__":
    main()
