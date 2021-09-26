from typing import List
from fastapi import APIRouter,status, HTTPException,Depends
from sql_app import schemas,main,crud
from sql_app.database import SessionLocal, engine
from sqlalchemy.orm import Session

router = APIRouter(prefix="/auth")

@router.get("/isalive", tags=["Amigos"])
async def getIsAlive():
    return {'yes'}

@router.get("/amigos/{id_amigo}", response_model = List[schemas.Amigos_Get], status_code=status.HTTP_200_OK )
def get_amigos(id_amigo:int, db: Session = Depends(main.get_db)):
    try:
        amigo = crud.get_amigos(db, id_amigo)
        return amigo
    except:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Amigos no encontrados")
