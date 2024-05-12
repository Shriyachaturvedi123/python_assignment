# main.py

from fastapi import FastAPI, HTTPException
from models import Post, Comment, LikeDislike
from db import BlogDB

app = FastAPI()
blog_db = BlogDB(url="mongodb://localhost:27017/", db_name="blog")

@app.post("/posts/")
def create_post(post: Post):
    post_id = blog_db.create_post(post)
    return {"post_id": post_id}

# Implement other endpoints for CRUD operations on posts, comments, and likes/dislikes
