#fastapi helps us to create backend server

from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
async def hello():
    return "welcome to fastapi"

@app.get("/hello/{name}")
async def hello(name):
    return f"welcome to fastapi {name}"


# In order to run the app, open cmd in the project folder and run the command :
# uvicorn main:app --reload
# or uvicorn main:app --reload --host 0.0.0.0