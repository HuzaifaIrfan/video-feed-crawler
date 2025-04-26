# tasks/math_tasks.py
from celery_app import app

from database import Database
from crawler import Crawler

@app.task(name='tasks.crawler_tasks.crawl_pages')  # <<< Important!
def crawl_pages():
    
    pages=Database().get_pages()
    
    inserted_video_ids=[]
    
    for page in pages:
        title = page['title']
        url = page['url']
    
        videos=Crawler().get_videos(url)
        
        
        
        for video in videos:
            try:
                inserted_video_id=Database().insert_video(video["uid"],video["title"],video["img"])
                inserted_video_ids.append(inserted_video_id)
            except:
                print(f"Cant Insert Video {video["uid"]}")
                
    print(inserted_video_ids)
    
    return inserted_video_ids


