from fastapi import APIRouter

router = APIRouter()



@router.get("/isalive", tags=["Amigos"])
async def getIsAlive():
    return {'yes'}