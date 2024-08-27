import subprocess
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def sherlock(q: str):
    names = q.split(' ')
    result = subprocess.run(['sherlock'] + names,
                            capture_output=True, text=True)
    return {"result": result.stdout}
