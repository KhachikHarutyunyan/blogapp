import uvicorn
from fastapi import FastAPI

app = FastAPI(title="CI/CD Intro")


@app.get("/")
async def greating():
    return {"result": "Hello from APP"}

if __name__ == "__main__":
    uvicorn.run("main:app", workers=2, port=80, host="0.0.0.0")
