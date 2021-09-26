# CRUD: CREATE, READ, UPDATE, DELETE

from sqlalchemy.orm import Session
from . import models, schemas
from sqlalchemy.exc import SQLAlchemyError

def get_categoria(db: Session, categoria_id: int):
    return db.\
        query(models.Categoria).\
        filter(models.Categoria.id == categoria_id).\
        first()

def get_categorias(db: Session, skip: int = 0, limite: int = 100):
    return db.\
        query(models.Categoria).\
        offset(skip).\
        limit(limite).\
        all() # limit top

# ==================================================================================================

def get_editorial(db: Session, editorial_id: int):
    return db.query(models.Editorial).filter(models.Editorial.id == editorial_id).all()

def get_editoriales(db: Session, offset: int = 0, limite: int = 100):
    return db.\
        query(models.Editorial).\
        offset(offset).\
        limit(limite).\
        all()

# ======================================================================================================

def get_libros(db: Session, offset: int = 0, limite: int = 100):
    return db.\
        query(models.Libro).\
        offset(offset).\
        limit(limite).\
        all()

def get_libros_by_autor(db: Session, id_autor: int ):
    return db.query(models.Autor).filter(models.Autor.id == id_autor).first().libros

def get_libros_by_editorial(db: Session, id_editorial: int ):
    return db.query(models.Editorial).filter(models.Editorial.id == id_editorial).first().libros

def get_libros_by_categoria(db: Session, id_categoria: int ):
    return db.query(models.Categoria).filter(models.Categoria.id == id_categoria).first().libros
#=======================================================================================================================

# ============================================================================================================

def crear_cliente(db: Session, nuevo_cliente: schemas.Cliente_Post):
    try:
        db_cliente = models.Cliente(nombre=nuevo_cliente.nombre,
                                    apellidos=nuevo_cliente.apellidos,
                                    correo=nuevo_cliente.correo)
        db.add(db_cliente)
        db.commit()
        db.refresh(db_cliente)
        return db_cliente
    except SQLAlchemyError as exc:
        db.rollback()
        raise Exception(message="Error creando el registro")


def actualizar_cliente(db: Session, cliente_actualizado: schemas.Cliente_Post, id_cliente: int):
    viejo_cliente = db.query(models.Cliente).filter(models.Cliente.id == id_cliente)

    if not viejo_cliente.first():
        raise SQLAlchemyError(message="Error encontrando el registro para actualizar")

    print(cliente_actualizado.dict())
    viejo_cliente.update(cliente_actualizado.dict())
    db.commit()

    return viejo_cliente.first()

def borrar_cliente(db: Session, id_cliente: int):
    cliente = db.query(models.Cliente).filter(models.Cliente.id == id_cliente)

    if not cliente.first():
        raise SQLAlchemyError(message= "Error encontrando el registro para borrar")

    cliente.delete(synchronize_session=False)
    db.commit()

    return id_cliente