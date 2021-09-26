from fastapi import APIRouter

router = APIRouter()



@router.get("/isalive")
async def getIsAlive():
    return {'yes'}