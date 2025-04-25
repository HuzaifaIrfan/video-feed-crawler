from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv(override=True)

# Access environment variables
SELENIUM_URL = os.getenv("SELENIUM_URL", "http://localhost:4444/wd/hub")
print(f"SELENIUM_URL at '{SELENIUM_URL}'")

from selenium import webdriver
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

class Crawler:
    _instance = None

    def __new__(cls, *args, **kwargs):
        # Create the instance only if it doesn't exist
        if cls._instance is None:
            cls._instance = super(Crawler, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):  # To ensure initialization happens only once
            self.initialized = True

            
    def get_driver(self):
        
        print("Get Driver")
        
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        # options.add_argument('headless')
        
        # Connect to the Selenium standalone container
        driver = webdriver.Remote(
            command_executor=SELENIUM_URL,  # Or replace 'localhost' with the container host
            options=options
        ) 
  
        print("Got Driver")
        
        return driver
      
        
    def get_body(self,url:str):
        
        print(f"crawler driver get_body {url}")
        
        body=""
        
        try:
            
            driver=self.get_driver()
        
            driver.get(url)

            title = driver.title

            # self.driver.implicitly_wait(20)

            print(title)
            
            body=driver.execute_script("return document.body.innerHTML;")
            
            
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if driver:
                driver.quit()
        
        return body
        

    def get_yt_videos(self, url:str) -> list:
        
        body=self.get_body(url)
        
        soup = BeautifulSoup(body, "html.parser")
        videos_soups=soup.find_all('ytd-rich-item-renderer')
        print(f"videos_soups {len(videos_soups)}")
        videos=[]
        
        
        for video_soup in videos_soups:
            title = video_soup.find(id="video-title").text
            link=video_soup.find(id="video-title-link").get('href', None)
            uid=link.split("/watch?v=")[1].split("&")[0]
            img_src=video_soup.find("img").get('src', None)
            
            if not img_src:
                continue
            
            video={
                "uid": uid,
                "title":title,
                "img":img_src,
            }
                    
            print(video)
            
            videos.append(video)
            
        return videos
                    
if __name__ == "__main__":
    crawler=Crawler()
    print(crawler)


