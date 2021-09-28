from typing import List
from fastapi import APIRouter,status, HTTPException,Depends
from sql_app import schemas,main,crud
from sql_app.database import SessionLocal, engine
from sqlalchemy.orm import Session
from authentication.auth2 import check_jwt_token

router = APIRouter()

router = APIRouter(prefix="/AMIGOS", dependencies=[Depends(check_jwt_token)])

@router.get("/isalive", tags=["Amigos"])
async def getIsAlive():
    '''
       Permite verificar que la API esta funcionando correctamente
       con un mensaje predeterminado.
       '''
    return {'yes'}

@router.get("/amigo/{id_amigo}", response_model = List[schemas.Amigos_Get], status_code=status.HTTP_200_OK , tags=["Amigos"])
def get_amigos(id_amigo:int, db: Session = Depends(main.get_db)):
    '''
        Permite verificar quienes son los contactos que
        intervienen en un mensaje cualquiera a traves de
        un estatus, fecha asociación y una llave cifrada para
        el envio seguro del mensaje.
        '''
    try:
        amigo = crud.get_Amigos(db, id_amigo)
        return amigo
    except:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Amigos no encontrados")

@router.get("/amigoAll", response_model = List[schemas.Amigos_Get], status_code=status.HTTP_200_OK, tags=["Amigos"] )
def get_amigosAll(offset: int = 0, limite: int = 100, db: Session = Depends(main.get_db)):
    '''
        Permite verificar todos los registros relacionados aquienes son
        los contactos que intervienen en un mensaje cualquiera a traves
        visualizando su estatus, fecha asociación y una llave cifrada
        utilizada para el envio seguro del mensaje.
        '''
    try:
        amigo = crud.get_Amigos_All(db, offset, limite)
        return amigo
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Amigos no encontrados")

@router.post("/amigo", status_code=status.HTTP_201_CREATED, tags=["Amigos"])
async def crear_amigos(nuevo_amigo: schemas.Amigos_Post, db: Session = Depends(main.get_db)):
    '''
       Permite registrar en la tabla amigos con formato Jason
       los contactos que van a intervienen en el mensaje indicando
       campos como llave cifrada, fecha y se registrara los intentos
       fallidos del ingreso de un servicio.
       '''
    try:
        result = crud.crear_Amigos(nuevo_amigo=nuevo_amigo, db=db)
        return {"id": result.id, "status": "ok"}
    except:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Amigo no agregado")

@router.put("/amigo/{id}", status_code=status.HTTP_202_ACCEPTED, tags=["Amigos"])
async def actualizar_amigo(id: int, amigo_actualizado: schemas.Amigos_Post, db: Session = Depends(main.get_db)):
     try:
         result = crud.actualizar_Amigos(amigo_actualizado=amigo_actualizado, db=db, id=id)
         return {"id": result.id, "status": "ok"}
     except:
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Amigo no actualizado")

@router.delete("/amigo/{id}", status_code=status.HTTP_200_OK , tags=["Amigos"])
async def borrar_amigo(id: int, db: Session = Depends(main.get_db)):
    '''
       Permite la eliminación permanente de un registro de amigos
       a traves del un filtro de identicacion de la tabla.
       '''
    try:
        result = crud.borrar_Amigos(db = db, id_amigo = id)
        return {"id": str(result), "status": "ok", "operacion": "delete_amigo"}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Amigo no borrado")
