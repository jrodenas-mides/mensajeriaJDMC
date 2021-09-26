# CRUD: CREATE, READ, UPDATE, DELETE

from sqlalchemy.orm import Session
from . import models, schemas
from sqlalchemy.exc import SQLAlchemyError


def get_Amigos_All(db: Session, offset: int = 0, limite: int = 100):
    return db.\
        query(models.Amigos).\
        offset(offset).\
        limit(limite).\
        all()

def get_Amigos(db: Session, Amigos_id: int):
    return db.\
        query(models.Amigos).\
        filter(models.Amigos.Id == Amigos_id).\
        first()

def crear_Amigos(db: Session, nuevo_Amigo: schemas.Amigos_Post):
    try:
        db_Amigos = models.Amigos(Id_Contacto1=nuevo_Amigo.id_contacto1,
                                    Id_Contacto2=nuevo_Amigo.id_contacto2,
                                    Id_Estatus=nuevo_Amigo.id_estatus,
                                    Fecha_Asociacion=nuevo_Amigo.fecha_asociacion,
                                    Llave_Cifrada=nuevo_Amigo.llave_cifrada)
        db.add(db_Amigos)
        db.commit()
        db.refresh(db_Amigos)
        return db_Amigos
    except SQLAlchemyError as exc:
        db.rollback()
        raise Exception(message="Error creando el registro")


def actualizar_Amigos(db: Session, Amigos_actualizado: schemas.Amigos_Post, id: int):
    viejo_Amigos = db.query(models.Amigos).filter(models.Amigos.Id == id)

    if not viejo_Amigos.first():
        raise SQLAlchemyError(message="Error encontrando el registro para actualizar")

    print(Amigos_actualizado.dict())
    viejo_Amigos.update(Amigos_actualizado.dict())
    db.commit()

    return viejo_Amigos.first()


def borrar_Amigos(db: Session, id_Amigo: int):
    Amigo = db.query(models.Amigos).filter(models.Amigos.Id == id_Amigo)

    if not Amigo.first():
        raise SQLAlchemyError(message= "Error encontrando el registro para borrar")

    Amigo.delete(synchronize_session=False)
    db.commit()

    return id_Amigo