# import os
# # Set environment variable
# os.environ["DATABASE"] = "video_feed_crawler_test"

from database import Database
from crawler import Crawler
    

def test_crawl_and_insert_list():
    
    Database().clean()
    
    pages_test=[
        # {
        #     "title":"NetworkChuck",
        #     "url":"https://www.youtube.com/@NetworkChuck/videos",
        # },
        # {
        #     "title":"ThePrimeTimeagen",
        #     "url":"https://www.youtube.com/@ThePrimeTimeagen/videos",
        # },
        # {
        #     "title":"TravisMedia",
        #     "url":"https://www.youtube.com/@TravisMedia/videos",
        # },
                        
        # {
        #     "title":"TheCodingSloth",
        #     "url":"https://www.youtube.com/@TheCodingSloth/videos",
        # },
                                
        # {
        #     "title":"TechWorldwithNana",
        #     "url":"https://www.youtube.com/@TechWorldwithNana/videos",
        # },
                                        
        # {
        #     "title":"Fireship",
        #     "url":"https://www.youtube.com/@Fireship/videos",
        # },
                                                
        # {
        #     "title":"IBMTechnology",
        #     "url":"https://www.youtube.com/@IBMTechnology/videos",
        # },
                                                        
        {
            "title":"Computerphile",
            "url":"https://www.youtube.com/@Computerphile/videos",
        },
        {
            "title":"Hussein Nasser",
            "url":"https://www.youtube.com/@hnasr/videos"
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
