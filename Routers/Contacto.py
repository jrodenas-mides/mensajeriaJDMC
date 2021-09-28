from typing import List
from fastapi import APIRouter,status, HTTPException,Depends
from sql_app import schemas,main,crud
from sql_app.database import SessionLocal, engine
from sqlalchemy.orm import Session


router = APIRouter()

@router.get("/isalive", tags=["Contacto"])
async def getIsAlive():
    return {'yes'}

@router.get("/contacto/{id_contacto}", response_model = List[schemas.contactos_Get], status_code=status.HTTP_200_OK , tags=["Contacto"])
def get_Contacto(id_contacto:int, db: Session = Depends(main.get_db)):
    try:
        contacto1 = crud.get_Contacto(db, id_contacto)
        return contacto1
    except:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contacto no encontrados")

@router.get("/contactoAll", response_model = List[schemas.contactos_Get], status_code=status.HTTP_200_OK, tags=["Contacto"] )
def get_Contactos_All(offset: int = 0, limite: int = 100, db: Session = Depends(main.get_db)):
    try:
        contacto = crud.get_Contactos_All(db, offset, limite)
        return contacto
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contacto no encontrados")

@router.post("/contacto", status_code=status.HTTP_201_CREATED, tags=["Contacto"])
async def crear_Contacto(nuevo_contacto: schemas.contactos_Post, db: Session = Depends(main.get_db)):
    try:
        result = crud.crear_Contacto(nuevo_contacto=nuevo_contacto, db=db)
        return {"id": result.id, "status": "ok"}
    except:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="contacto no agregado")

@router.put("/contacto/{id}", status_code=status.HTTP_202_ACCEPTED, tags=["Contacto"])
async def actualizar_Contactos(id: int, contacto_actualizado: schemas.contactos_Post, db: Session = Depends(main.get_db)):
     try:
         result = crud.actualizar_Contactos(contacto_actualizado=contacto_actualizado, db=db, id_contacto=id)
         return {"id": result.id, "status": "ok"}
     except:
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="contacto no actualizado")

@router.delete("/contacto/{id}", status_code=status.HTTP_200_OK , tags=["Contacto"])
async def borrar_Contactos(id: int, db: Session = Depends(main.get_db)):
    try:
        result = crud.borrar_Contactos(db = db, id_contacto = id)
        return {"id": str(result), "status": "ok", "operacion": "delete_contacto"}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contacto no borrado")
