# db.py

from pymongo import MongoClient
from bson.objectid import ObjectId
from models import Post, Comment, LikeDislike

class BlogDB:
    def __init__(self, url: str, db_name: str):
        self.client = MongoClient(url)
        self.db = self.client[db_name]

    def create_post(self, post: Post) -> str:
        result = self.db.posts.insert_one(post.dict())
        return str(result.inserted_id)

    # Implement methods for CRUD operations on posts, comments, and likes/dislikes
