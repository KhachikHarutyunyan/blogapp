import os

import uvicorn
from fastapi import FastAPI

app = FastAPI(title="CI/CD Intro")


@app.get("/")
async def greating():
    env = (os.getenv("RUNNER_PATH"))
    return {"result": f"Hello from APP:::{env}"}

if __name__ == "__main__":
    uvicorn.run("main:app", workers=2, port=80, host="0.0.0.0")
