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
        filter(models.Amigos.id == Amigos_id).\
        all()

def crear_Amigos(db: Session, nuevo_amigo: schemas.Amigos_Post):
    try:
        db_Amigos = models.Amigos(id_contacto1=nuevo_amigo.id_contacto1,
                                    id_contacto2=nuevo_amigo.id_contacto2,
                                    id_estatus=nuevo_amigo.id_estatus,
                                    fecha_asociacion=nuevo_amigo.fecha_asociacion,
                                    llave_cifrada=nuevo_amigo.llave_cifrada)
        db.add(db_Amigos)
        db.commit()
        db.refresh(db_Amigos)
        return db_Amigos
    except SQLAlchemyError as exc:
        db.rollback()
        raise Exception(message="Error creando el registro")


def actualizar_Amigos(db: Session, amigo_actualizado: schemas.Amigos_Post, id: int):
    viejo_Amigos = db.query(models.Amigos).filter(models.Amigos.id == id)

    if not viejo_Amigos.first():
        raise SQLAlchemyError(message="Error encontrando el registro para actualizar")

    print(amigo_actualizado.dict())
    viejo_Amigos.update(amigo_actualizado.dict())
    db.commit()

    return viejo_Amigos.first()


def borrar_Amigos(db: Session, id_amigo: int):
    Amigo = db.query(models.Amigos).filter(models.Amigos.id == id_amigo)

    if not Amigo.first():
        raise SQLAlchemyError(message= "Error encontrando el registro para borrar")

    Amigo.delete(synchronize_session=False)
    db.commit()

    return id_amigo

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
                                    correoelectronico=nuevo_contacto.correoelectronico,
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
    Contacto = db.query(models.Contactos).filter(models.Contactos.id == id_contacto)

    if not Contacto.first():
        raise SQLAlchemyError(message= "Error encontrando el registro para borrar")

    Contacto.delete(synchronize_session=False)
    db.commit()

    return id_contacto


#============================================================================================================
#MENSAJES


def get_Mensajeria_All(db: Session, offset: int = 0, limite: int = 100):
    return db.\
        query(models.Mensajes).\
        offset(offset).\
        limit(limite).\
        all()

def get_Mensajes(db: Session, Mensajes_id: int):
    return db.\
        query(models.Mensajes).\
        filter(models.Mensajes.id == Mensajes_id).\
        all()

def crear_Mensajes(db: Session, nuevo_mensaje: schemas.mensajes_Post):
    try:
        db_Mensajes = models.Mensajes(id_emisor=nuevo_mensaje.id_emisor,
                                    id_receptor=nuevo_mensaje.id_receptor,
                                    fecha_envio=nuevo_mensaje.fecha_envio,
                                    id_estatus=nuevo_mensaje.id_estatus,
                                    mensaje=nuevo_mensaje.mensaje)
        db.add(db_Mensajes)
        db.commit()
        db.refresh(db_Mensajes)
        return db_Mensajes
    except SQLAlchemyError as exc:
        db.rollback()
        raise Exception(message="Error creando el registro")


def actualizar_Mensajes(db: Session, mensaje_actualizado: schemas.mensajes_Post, id: int):
    viejo_Mensaje = db.query(models.Mensajes).filter(models.Mensajes.id == id)

    if not viejo_Mensaje.first():
        raise SQLAlchemyError(message="Error encontrando el registro para actualizar")

    print(mensaje_actualizado.dict())
    viejo_Mensaje.update(mensaje_actualizado.dict())
    db.commit()

    return viejo_Mensaje.first()


def borrar_Mensaje(db: Session, id_mensaje: int):
    Mensaje = db.query(models.Mensajes).filter(models.Mensajes.id == id_mensaje)

    if not Mensaje.first():
        raise SQLAlchemyError(message= "Error encontrando el registro para borrar")

    Mensaje.delete(synchronize_session=False)
    db.commit()

    return id_mensaje
