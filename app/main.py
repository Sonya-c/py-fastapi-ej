# following this tutorial: https://www.youtube.com/watch?v=0sOvCWFmrtA&t=2061s

from random import randrange
from typing import Optional
from fastapi import Body, FastAPI, HTTPException, Response, status
from pydantic import BaseModel

# built-in documentation: 
# swager /docs
# redoc /redoc

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

posts = [
    {
        "title":"Title Post 1",
        "body":"Body post 1",
        "id":1,
    },
    {
        "title":"Title Post 2",
        "body":"Body post 2",
        "id":2,
    }
]    

# Path (or route) operation 
@app.get("/") # decorator "magic to the function"
# app.http method(path)
def root(): # function 
    # return: data get back to user
    # dict -> json (fastapi)
    return {"message":"Hello World!"}

# Note: The order matters (sometimes)

# Read 
# why plural? its a convention
@app.get("/posts")
def get_posts():
    return {"data": posts} # auto serialize it

@app.get("/posts/{id}")
# note: all parms are string unless you specify the type
def get_post(id: int): # ✨ Automatic ✨, response: Response
    for post in posts: 
        if (post["id"] == id):
            return {"found" : True, "data": post}
    
    # response.status_code = status.HTTP_404_NOT_FOUND
    # return {"found": False, "data": None }
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Post with id = {id} was not found"
    )

# Create
# post requests (standar) 
@app.post("/posts", status_code=status.HTTP_201_CREATED) # post: we can send data to the server 
def create_post(post:Post): # as we use a model, fastApi gonna validate this
    print(f"title= {post.title}") # it automatically extract the data
    
    post_dict = post.model_dump()
    post_dict["id"] = randrange(0, 10**4)
    posts.append(post_dict)
    
    # it the data it's invalid, fastAPI send an error msg
    # it we recive an number, we can convert to string, so still working 
    return {
        "message": "Post created sucessfull",
        "post": post_dict,
    }

# Update
# put vs patch (it dosent matter, it's a preference)
# put: send all the info and change all
# patch: send an specific field and change it
@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    for index, og_post in enumerate(posts): 
        if (og_post["id"] == id):
            posts[index] = post.model_dump()
            posts[index]["id"] = id
        
        return {
            "message": "Post update sucessfull",
            "post": posts[index],
        }
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Post with id = {id} was not found"
    )


# Delete
# standart status code: 204 (no content) 
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    for index, post in enumerate(posts): 
        if (post["id"] == id):
            posts.pop(index)
            return None
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Post with id = {id} was not found"
    )
