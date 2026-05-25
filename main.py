from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"text":"you just got home"}