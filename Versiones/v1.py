from fastapi import FastAPI

app_v1 = FastAPI()

@app_v1.get("/isalive")
async def getIsAlive():
    return {'yes'}