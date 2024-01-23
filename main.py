from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Hello World, by Gita_Wardani & Kiki_Amalia"}
    