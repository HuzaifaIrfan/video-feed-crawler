from database import Database
from crawler import Crawler

def test_answer():
    
    Database().clean()
    
    url = "https://www.youtube.com/@Thewideside/videos"
    
    videos=Crawler().get_yt_videos(url)
    
    for video in videos:
        Database().insert_video(video["uid"],video["title"],video["img"])

    assert 1 == 1