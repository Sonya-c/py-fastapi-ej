from fastapi import Body, FastAPI 

app = FastAPI() # Create an instance

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

@app.post("/posts") # post: we can send date to the server 
def create_post(payload: dict = Body):
    print(payload)
    return {
        "message": "Post created sucessfull",
        "post": payload,
    }