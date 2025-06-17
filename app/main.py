from fastapi import FastAPI, Body , Response , HTTPException
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
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
       raise HTTPException(status_code=404, 
                           detail=f"Post with id: {id} not found")
    return {"post": post}

@app.delete("/posts/{id}")
def delete_post(id: int , status_code: int = 204):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=404, 
                            detail=f"Post with id: {id} not found")
    my_posts.remove(post)
    return Response(status_code=status_code, 
                    content="Post deleted successfully") 

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    post_dict = post.dict()
    existing_post = find_post(id)
    if not existing_post:
        raise HTTPException(status_code=404, 
                            detail=f"Post with id: {id} not found")
    
    existing_post.update(post_dict)
    return {"message": "Post updated successfully", "post": existing_post} 