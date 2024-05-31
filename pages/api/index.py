from fastapi import FastAPI

app = FastAPI()

@app.get("/api/hello")
async def home():
    return {"Response" : "Hello World!!!"}
