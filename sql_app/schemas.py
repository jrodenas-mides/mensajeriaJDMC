from pydantic import BaseModel

# POST
class Categoria_Post(BaseModel):
    nombre: str
    class Config:
        orm_mode = True


# GET
class Categoria_Get(Categoria_Post): # Categoria_Get hereda de Categoria_Post
    id: int

# =====================================================================================================================

class Editorial_Post(BaseModel):
    nombre: str
    pais: str
    class Config:
        orm_mode = True

class Editorial_Get(Editorial_Post):
    id: int

# ====================================================================================================================

class Libro_Post(BaseModel):
    nombre: str
    id_autor: int
    id_categoria: int
    precio: float
    edicion: str
    id_editorial: int
    anio_impresion: int

    class Config:
        orm_mode = True


class Libro_Get(Libro_Post):
    id: int


# ===============================================================================================

class Cliente_Post(BaseModel):
    nombre: str
    apellidos: str
    correo: str

    class Config:
        orm_mode = True


class Cliente_Get(Cliente_Post):
    id: int