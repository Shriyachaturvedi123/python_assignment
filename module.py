# models.py

from pydantic import BaseModel
from typing import List, Optional

class Post(BaseModel):
    title: str
    content: str
    author: str

class Comment(BaseModel):
    text: str
    author: str

class LikeDislike(BaseModel):
    user: str
    action: str  # 'like' or 'dislike'
