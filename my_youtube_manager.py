import json


def load_data():
    try :
        with open("youtube.txt","r") as file :
            return json.load(file)
    except FileNotFoundError :
        return[]
def save_data_helper(videos):
    with open("youtube.txt","w") as file :
        json.dump(videos,file)

def list_all_videos(videos):
    print("\n")
    print("*"*70)
    for index ,video in enumerate(videos,start=1):
        print(f"{index}.{video['name']},duration: {video['time']}, ")
    print("\n")
    print("*"*70)
def add_video(videos):
    name = input('enter video title: ')
    time = input('enter video time: ')
    videos.append({"name" :name,"time":time})
    save_data_helper(videos)
def update_video(videos):
    list_all_videos(videos)
    index = int(input("enter new video number to update : "))
    if 1 <= index <= len(videos):
        name = input(" enter the video name: ")
        time = input("enter video time : ")
        videos[index-1] = {"name":name,"time":time}
        save_data_helper(videos)
    else:
        print("invalid index selected")


def remove_video(videos):
    list_all_videos(videos)
    index = int(input("enter new video number to delete : "))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
def main():
    videos =load_data()
    while True :
        print("Welcome to Youtube Manager")
        print("1. list all youtube video ")
        print("2. add a video ")
        print("3. update a video ")
        print("4. remove a video ")
        print("5. exit")
        choice = input("Enter your choice : ")
        # print(videos)
        match choice :
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                remove_video(videos)
            case "5":
                break
            case _ :
                print("invalid choice")
if __name__ == "__main__":
    main()
