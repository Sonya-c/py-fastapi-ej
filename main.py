from fastapi import FastAPI 

app = FastAPI() # Create an instance

# Path (or route) operation 
@app.get("/") # decorator "magic to the function"
# app.http method(path)
def root(): # function 
    # return: data get back to user
    # dict -> json (fastapi)
    return {"message":"Hello World!"}
