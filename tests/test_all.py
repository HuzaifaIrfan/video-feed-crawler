# import os
# # Set environment variable
# os.environ["DATABASE"] = "video_feed_crawler_test"

from database import Database
from crawler import Crawler
    

def test_crawl_and_insert_list():
    
    Database().clean()
    
    pages_test=[
        {
            "title":"Thewideside",
            "url":"https://www.youtube.com/@Thewideside/videos"
        },
        {
            "title":"WildlensbyAbrar",
            "url":"https://www.youtube.com/@WildlensbyAbrar/videos",
        },
        {
            "title":"Computerphile",
            "url":"https://www.youtube.com/@Computerphile/videos",
        },
        {
            "title":"EonUpdates",
            "url":"https://www.youtube.com/@EonUpdates/videos"
        }
    ]
    
    for page in pages_test:
        Database().insert_page(**page)
    
    pages=Database().get_pages()
    
    for page in pages:
        title = page['title']
        url = page['url']
    
        videos=Crawler().get_videos(url)
        
        for video in videos:
            Database().insert_video(video["uid"],video["title"],video["img"])
