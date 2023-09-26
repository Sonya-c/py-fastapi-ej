from typing import Optional
from fastapi import Body, FastAPI 
from pydantic import BaseModel

app = FastAPI() # Create an instance

# schema: contract client-server, so the client send you the expected data
# we're gonna use pydantic
# schema:
#    title: srt
#    content: srt

class Post(BaseModel):
    title: str 
    body: str = "" # we can set body as optional field
    rating: Optional[int] = None # fully optional field 
    
# Path (or route) operation 
@app.get("/") # decorator "magic to the function"
# app.http method(path)
def root(): # function 
    # return: data get back to user
    # dict -> json (fastapi)
    return {"message":"Hello World!"}

# Note: The order matters (sometimes)

@app.get("/posts")
def get_post():
    return {"message": "All post"}

@app.post("/posts") # post: we can send data to the server 
def create_post(post:Post): # as we use a model, fastApi gonna validate this
    print(f"title= {post.title}") # it automatically extract the data

    # it the data it's invalid, fastAPI send an error msg
    # it we recive an number, we can convert to string, so still working 
    return {
        "message": "Post created sucessfull",
        "post": post,
    }

