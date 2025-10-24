import os

import uvicorn
from fastapi import FastAPI

app = FastAPI(title="CI/CD Intro GIT_HUB")


@app.get("/")
async def greating():
    env = (os.getenv("RUNNER_PATH"))
    return {"detail": f"Hello from APP:::{env}"}

@app.get("/health")
async def health():
    return {"detail": "Healthy"}

if __name__ == "__main__":
    uvicorn.run("main:app", workers=2, port=80, host="0.0.0.0")
