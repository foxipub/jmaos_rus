from typing import (Deque, Dict, FrozenSet, List, Optional, Sequence, Set, Tuple, Union)
from fastapi import FastAPI
from pydantic import BaseModel



app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = []


@app.get("/")
async def root():
    return {"message": "Hello world"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post)
    new_post.dict()
    return {"data": new_post}
# title str, content str
