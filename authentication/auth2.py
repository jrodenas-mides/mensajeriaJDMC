import time
from datetime import datetime, timedelta

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from sqlalchemy.orm import Session

import sql_app.models as models
import sql_app.schemas as schemas
from authentication.constants import JWT_EXPIRATION_TIME_MINUTES, JWT_SECRET_KEY, JWT_ALGORITHM, JWT_VALID_ROLES
from sql_app import main as sqlORM

pwd_context = CryptContext(schemes=["bcrypt"])
oauth_schema = OAuth2PasswordBearer(tokenUrl="/token")


def get_hashed_password(plain_password: str):
    return pwd_context.hash(plain_password)


def verify_password(plain_password: str, hashed_password: str):
    try:
        return pwd_context.verify(plain_password, hashed_password)
    except:
        return False

# 1. Autenticar un usuario:
def authenticate_user(user: schemas.contactos_Get, db: Session = Depends(sqlORM.get_db)):
    usuario = db.query(models.Contactos).filter(models.Contactos.usuario == user.usuario)

    if not usuario.first():
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuario no existe en la bd")

    user_in_db = usuario.first()
    if verify_password(user.jwtoken, user_in_db.jwtoken):
        return user_in_db

    return None


# ======================================================================================================================

# 2. Crear el jwt_token:

def create_jwt_token(user: schemas.contactos_Get):
    expiration = datetime.utcnow() + timedelta(minutes=JWT_EXPIRATION_TIME_MINUTES)

    jwt_payload = {
        "usr": user.usuario,
        "rol": user.idrol,
        "exp": expiration
    }

    jwt_token = jwt.encode(payload=jwt_payload, key=JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return jwt_token

# ======================================================================================================================

# 3. Chequear si el JWT es correcto:

def check_jwt_token(token: str = Depends(oauth_schema), db: Session = Depends(sqlORM.get_db)):
    try:
        payload = jwt.decode(jwt=token, key=JWT_SECRET_KEY, algorithms=JWT_ALGORITHM)
        username = payload.get("usr")
        rol = payload.get("rol")
        exp = payload.get("exp")

        if time.time() < exp:
            if user_exist_in_db(username, db=db):
                return validar_rol(rol)

    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token invalido")

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token no pasa las validaciones")

# ======================================================================================================================

# 4. Validar Authorizaciones y otras cosas...

def validar_rol(rol: str):
    if rol in JWT_VALID_ROLES:
        return True
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Rol Invalido")
