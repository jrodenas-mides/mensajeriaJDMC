# CRUD: CREATE, READ, UPDATE, DELETE

from sqlalchemy.orm import Session
from . import models, schemas
from sqlalchemy.exc import SQLAlchemyError


#==============================================================================================================
#AMIGOS

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
        all()

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

#==============================================================================================
#CONTACTOS

def get_Contactos_All(db: Session, offset: int = 0, limite: int = 100):
    return db.\
        query(models.Contactos).\
        offset(offset).\
        limit(limite).\
        all()

def get_Contacto(db: Session, Contacto_id: int):
    return db.\
        query(models.Contactos).\
        filter(models.Contactos.id == Contacto_id).\
        all()

def crear_Contacto(db: Session, nuevo_contacto: schemas.contactos_Post):
    try:
        db_Contactos = models.Contactos(usuario=nuevo_contacto.usuario,
                                    nombres=nuevo_contacto.nombres,
                                    apellidos=nuevo_contacto.apellidos,
                                    correoElectronico=nuevo_contacto.correoelectronico,
                                    telefono=nuevo_contacto.telefono,
                                    genero=nuevo_contacto.genero,
                                    fechanacimiento=nuevo_contacto.fechanacimiento,
                                    jwtoken=nuevo_contacto.jwtoken,
                                    intentosfallidos=nuevo_contacto.intentosfallidos,
                                    fechabloqueo=nuevo_contacto.fechabloqueo,
                                    idrol=nuevo_contacto.idrol)
        db.add(db_Contactos)
        db.commit()
        db.refresh(db_Contactos)
        return db_Contactos
    except SQLAlchemyError as exc:
        db.rollback()
        raise Exception(message="Error creando el registro")


def actualizar_Contactos(db: Session, contacto_actualizado: schemas.contactos_Post, id_contacto: int):
    viejo_Contacto = db.query(models.Contactos).filter(models.Contactos.id == id_contacto)

    if not viejo_Contacto.first():
        raise SQLAlchemyError(message="Error encontrando el registro para actualizar")


    viejo_Contacto.update(contacto_actualizado.dict())
    db.commit()

    return viejo_Contacto.first()


def borrar_Contactos(db: Session, id_contacto: int):
    Contacto = db.query(models.Contactos).filter(models.Contactos.Id == id_contacto)

    if not Contacto.first():
        raise SQLAlchemyError(message= "Error encontrando el registro para borrar")

    Contacto.delete(synchronize_session=False)
    db.commit()

    return id_contacto


#============================================================================================================
#MENSAJES

def get_Mensajes_All(db: Session, offset: int = 0, limite: int = 100):
    return db.\
        query(models.Mensajes).\
        offset(offset).\
        limit(limite).\
        all()

def get_Mensajes(db: Session, Mensaje_id: int):
    return db.\
        query(models.Mensajes).\
        filter(models.Mensajes.Id == Mensaje_id).\
        all()

def crear_Mensaje(db: Session, nuevo_Mensaje: schemas.mensajes_Post):
    try:
        db_Mensaje = models.Mensajes(Id_Emisor=nuevo_Mensaje.Id_Emisor,
                                    Id_Receptor=nuevo_Mensaje.Id_Receptor,
                                    Fecha_Envio=nuevo_Mensaje.Fecha_Envio,
                                    Id_Estatus=nuevo_Mensaje.Id_Estatus,
                                    Mensaje=nuevo_Mensaje.Mensaje)
        db.add(db_Mensaje)
        db.commit()
        db.refresh(db_Mensaje)
        return db_Mensaje
    except SQLAlchemyError as exc:
        db.rollback()
        raise Exception(message="Error creando el registro")


def actualizar_Mensajes(db: Session, Mensaje_actualizado: schemas.mensajes_Post, id: int):
    viejo_Mensaje = db.query(models.Mensajes).filter(models.Mensajes.Id == id)

    if not viejo_Mensaje.first():
        raise SQLAlchemyError(message="Error encontrando el registro para actualizar")

    print(Mensaje_actualizado.dict())
    viejo_Mensaje.update(Mensaje_actualizado.dict())
    db.commit()

    return viejo_Mensaje.first()


def borrar_Mensajes(db: Session, id_Mensaje: int):
    Mensaje = db.query(models.Mensajes).filter(models.Mensajes.Id == id_Mensaje)

    if not Mensaje.first():
        raise SQLAlchemyError(message= "Error encontrando el registro para borrar")

    Mensaje.delete(synchronize_session=False)
    db.commit()

    return id_Mensaje


