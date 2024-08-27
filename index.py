import subprocess
from fastapi import FastAPI

app = FastAPI()

@app.get("/sherlock")
def sherlock(q: str):
    names = q.split(' ')
    result = subprocess.run(['sherlock'] + names,
                            capture_output=True, text=True)
    return {"result": result.stdout}

@app.get("/")
def main():
    return "success"
