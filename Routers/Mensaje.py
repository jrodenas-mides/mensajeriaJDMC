from typing import List
from fastapi import APIRouter,status, HTTPException,Depends
from sql_app import schemas,main,crud
from sql_app.database import SessionLocal, engine
from sqlalchemy.orm import Session
from authentication.auth2 import check_jwt_token

router = APIRouter()
router = APIRouter(prefix="/MENSAJE", dependencies=[Depends(check_jwt_token)])

@router.get("/isalive", tags=["Mensaje"])
async def getIsAlive():
    '''
        Permite verificar que la API esta funcionando correctamente
        con un mensaje predeterminado.
        '''
    return {'yes'}

@router.get("/mensaje/{id_mensaje}", response_model = List[schemas.mensajes_Get], status_code=status.HTTP_200_OK , tags=["Mensaje"])
def get_mensaje(id_mensaje:int, db: Session = Depends(main.get_db)):
    '''
        Muestra tanto los dos contactos involucrados en la conversacion
        como el mensaje que se envio de manera secreta pero indicandole
        a traves de un ID un mensaje especifico
        '''
    try:
        mensaje = crud.get_Mensajes(db, id_mensaje)
        return mensaje
    except:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Amigos no encontrados")

@router.get("/mensajeAll", response_model = List[schemas.mensajes_Get], status_code=status.HTTP_200_OK, tags=["Mensaje"] )
def get_mensajeAll(offset: int = 0, limite: int = 100, db: Session = Depends(main.get_db)):
    '''
        Muestra tanto los dos contactos involucrados en la conversacion
        como el mensaje que se envio de manera secreta en su totalidad,
        es decir, todos los mensajes creados.
        '''
    try:
        mensaje = crud.get_Mensajeria_All(db, offset, limite)
        return mensaje
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Mensaje no encontrados")


@router.post("/mensaje", status_code=status.HTTP_201_CREATED, tags=["Mensaje"])
async def crear_mensaje(nuevo_mensaje: schemas.mensajes_Post, db: Session = Depends(main.get_db)):
    '''
        Permite registrar con un formato Jason el mensaje con
        un estoado ingresado y tambien a los conctactos que intervienen
        en dicha conversación.
        '''
    try:
        result = crud.crear_Mensajes( nuevo_mensaje =nuevo_mensaje, db=db)
        return {"id": result.id, "status": "ok"}
    except:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Amigo no agregado")


@router.put("/mensaje/{id}", status_code=status.HTTP_202_ACCEPTED, tags=["Mensaje"])
async def actualizar_mensaje(id: int, mensaje_actualizado: schemas.mensajes_Post, db: Session = Depends(main.get_db)):

     try:
         result = crud.actualizar_Mensajes(mensaje_actualizado =mensaje_actualizado, db=db, id=id)
         return {"id": result.id, "status": "ok"}
     except:
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Mensaje no actualizado")

@router.delete("/mensaje/{id}", status_code=status.HTTP_200_OK , tags=["Mensaje"])
async def borrar_mensaje(id: int, db: Session = Depends(main.get_db)):
    '''
        Permite eliminar un mensaje seleccionado a
        través de un ID
        '''
    try:
        result = crud.borrar_Mensaje(db = db, id_mensaje = id)
        return {"id": str(result), "status": "ok", "operacion": "delete_mensaje"}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Amigo no borrado")