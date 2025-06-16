from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Optional 
from random import randrange

app = FastAPI()

my_posts = [{"id": 1, "title": "Post 1", "content": "Content of post 1"},
            {"id": 2, "title": "Post 2", "content": "Content of post 2"} ]
class Post(BaseModel):
    id: Optional[int] = None
    title: str
    content: str 
    published: bool = True
    rating: Optional[int] = None   

def find_post(id):
    for post in my_posts:
        if post["id"] == id:
            return post    

@app.get("/")
def root():
    return {"message": "Goodbye World"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/post")
def create_post(post:Post):
   post_dict = post.dict()
   post.id = randrange(0, 1000000)
   post_dict['id'] = post.id
   my_posts.append(post_dict)
   return {"message": "Post created successfully", "post": post} 

@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    if not post:
        return  {"message": "Post not found"}
    return {"post": post}