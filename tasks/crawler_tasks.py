# tasks/math_tasks.py
from celery_app import app

@app.task(name='tasks.crawler_tasks.crawl_pages')  # <<< Important!
def crawl_pages():
    
    
    from database import Database
    from crawler import Crawler
    
    pages=Database().get_pages()
    
    for page in pages:
        title = page['title']
        url = page['url']
    
        videos=Crawler().get_videos(url)
        
        for video in videos:
            try:
                Database().insert_video(video["uid"],video["title"],video["img"])
            except:
                print(f"Cant Insert Video {video["uid"]}")


