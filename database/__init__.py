from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv(override=True)

# Access environment variables
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/")
print(f"MONGODB_URI at '{MONGODB_URI}'")

DATABASE = os.getenv("DATABASE", "video_feed_crawler")
print(f"DATABASE at '{DATABASE}'")


from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING
from pymongo.collection import Collection

import datetime


class Database:
    _instance = None

    def __new__(cls, *args, **kwargs):
        # Create the instance only if it doesn't exist
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):  # To ensure initialization happens only once
            self.initialized = True
            
            self.client = MongoClient(MONGODB_URI)
            self.db = self.client[DATABASE]
            self.pages_collection=self.get_pages_collection()       
            self.videos_collection=self.get_videos_collection()

                
    def get_pages_collection(self) -> Collection:
        collection_name = "pages"
        if collection_name not in self.db.list_collection_names():
            self.db.create_collection(collection_name)

        self.pages_collection = self.db[collection_name]

        # Ensure the compound index exists
        index_name = "cat_1_created_at_-1"
        existing_indexes = self.pages_collection.index_information()

        if index_name not in existing_indexes:
            self.pages_collection.create_index([("cat", ASCENDING), ("created_at", DESCENDING)], name=index_name)

        print(f"Collection '{collection_name}' and index are ready.")
        
        return self.pages_collection
    
    
    def get_videos_collection(self) -> Collection:
        collection_name = "videos"
        if collection_name not in self.db.list_collection_names():
            self.db.create_collection(collection_name)

        self.videos_collection = self.db[collection_name]
        

        # Ensure the compound index exists
        index_name = "cat_1_created_at_-1"
        existing_indexes = self.videos_collection.index_information()

        if index_name not in existing_indexes:
            self.videos_collection.create_index([("cat", ASCENDING), ("created_at", DESCENDING)], name=index_name)

        print(f"Collection '{collection_name}' and index are ready.")
        
        return self.videos_collection
    
    def clean_videos(self):
        
        self.videos_collection.drop()      
        self.videos_collection=self.get_videos_collection()
        
    def clean(self):
        
        self.pages_collection.drop()
        self.videos_collection.drop()
        
        self.pages_collection=self.get_pages_collection()       
        self.videos_collection=self.get_videos_collection()

        
    

    def insert_page(self,title:str,url:str,site:int=0,cat:int=0):
        
        if not title:
            return None
        
        if not url:
            return None
        
        page={
            "title":title,
            "url":url,
            "site":site,
            "cat":cat
        }

        page["created_at"]= datetime.datetime.now(tz=datetime.timezone.utc)

        page_id = self.pages_collection.insert_one(page).inserted_id
        print(f"page inserted {page_id}")
        
        return page_id
    
    
    def insert_video(self,uid:str,title:str,img:str,site:int=0,cat:int=0):
        
        if not uid:
            return None
        
        if not title:
            return None
        
        if not img:
            return None
        
        video={
            "_id": uid,
            "title":title,
            "img":img,
            "site":site,
            "cat":cat
        }
        

        
        video["created_at"]= datetime.datetime.now(tz=datetime.timezone.utc)
        
        video_id = self.videos_collection.insert_one(video).inserted_id
        print(f"video inserted {video_id}")
        
        return video_id

    def get_pages(self,cat:int=0):
        results = self.pages_collection.find(
        {"cat": cat}        # filter: where category == your_category_name
        ).sort(
        "created_at", -1               # sort: newest first (-1 = DESCENDING)
        ).limit(10)
        return results

if __name__ == "__main__":
    database=Database()
    print(database)


