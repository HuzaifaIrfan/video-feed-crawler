from crawler import Crawler
from database import Database

def main():
    print("Hello from video_feed_crawler!")
    
    url = "https://www.youtube.com/@Thewideside/videos"
    
    
    videos=Crawler().get_yt_videos(url)
    
    for video in videos:
        Database().insert_video(video["uid"],video["title"],video["img"])

    


if __name__ == "__main__":
    main()
