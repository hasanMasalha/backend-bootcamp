from fastapi import FastAPI
import uvicorn
import app.model as model
from app.jwt_handler import signJWT
posts = [
    {
        "id":1,
        "name": "user1",
        "classes": ["math","english"],
        "role": "student"
    },
    {
        "id":2,
        "name": "user2",
        "classes": ["math","arabic"],
        "role": "student"
    },
    {
        "id":3,
        "name": "user3",
        "classes": ["math","english", "arabic"],
        "role": "teacher"
    }
]
users = []

app = FastAPI()

@app.get("/", tags = ["test"])
def test():
    return {"hello","test"}

@app.get("/all_posts",tags = ["posts"])
def get_posts():
    return{"data" : posts}

@app.get("/post_by_id/{id}", tags = ["posts"])
def get_post_by_id(id: int):
    if id > len(posts):
        return {
            "ERROR " : "post with this id is invalid"
                }
    else:
        for post in posts:
            if post["id"] == id:
                return {
                "data":post
            } 

@app.post("/posts",tags = ["posts"])
def add_post(post : model.postSchema ):
    post.id = len(posts)+1
    posts.append(post.dict())
    return{
        "info": "post Added!"
    }