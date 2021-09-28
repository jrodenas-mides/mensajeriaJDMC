from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

import sql_app.models as models
from Routers.autenticados import JwAmigos, JwContacto
from Routers import Contacto, Amigos, Mensaje
from authentication.auth2 import authenticate_user, create_jwt_token, get_hashed_password, check_jwt_token
from sql_app.schemas import contactos_Get, contactos_Post
from sql_app import main as sqlORM

app_auth = FastAPI(root_path="/auth")

# incluimos las rutas con autenticación y autorizacion
app_auth.include_router(Amigos.router)
app_auth.include_router(Mensaje.router)
app_auth.include_router(Contacto.router)


@app_auth.get("/isalive")
async def is_alive(is_authorized: bool = Depends(check_jwt_token)):
    return {"alive": "yes", "is_authorized": is_authorized}


# ======================================================================================================================

@app_auth.post("/token")
async def login_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(sqlORM.get_db)):
    dict_form_data = {"id": 1, "usuario": form_data.username, "jwtoken": form_data.password ,"nombres": "asd", "apellidos":"asd","correoelectronico":"asd","telefono":"asd","genero":"asd","fechanacimiento":"2021-09-27","intentosfallidos":"0","fechabloqueo":"2021-09-27 23:06","idrol":"1"}
    jwt_user = contactos_Get(**dict_form_data)
    user = authenticate_user(jwt_user, db=db)

    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuario no autenticable")

    jwt_token = create_jwt_token(user)
    return {
        "access_token": jwt_token
    }


# ======================================================================================================================

@app_auth.post("/signin", status_code=status.HTTP_201_CREATED)
async def create_new_user(new_user: contactos_Post, db: Session = Depends(sqlORM.get_db)):
    try:
        hashed_password = get_hashed_password(new_user.jwtoken)
        new_user.jwtoken = hashed_password
        db_new_user = models.Contactos(**new_user.dict())
        db.add(db_new_user)
        db.commit()
        db.refresh(db_new_user)
        return {"status": "ok", "id": db_new_user.id, "operacion": "crear_usuario"}
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Error creando el usuario: " + str(exc))
