from fastapi import APIRouter

router = APIRouter(prefix="/auth")

@router.get("/isalive", tags=["Amigos"])
async def getIsAlive():
    return {'yes'}