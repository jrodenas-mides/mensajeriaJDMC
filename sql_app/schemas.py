from datetime import datetime, date


from pydantic import BaseModel

# POST


class Amigos_Post(BaseModel):
    id_contacto1: int
    id_contacto2: int
    id_estatus: int
    fecha_asociacion: datetime
    llave_cifrada: str
    class Config:
        orm_mode = True


# GET
class Amigos_Get(Amigos_Post): # Categoria_Get hereda de Categoria_Post
    id: int

# =====================================================================================================================

class CategoriasEstatus_Post(BaseModel):
    descripcion: str
    class Config:
        orm_mode = True

class CategoriasEstatus_Get(CategoriasEstatus_Post):
    id: int

# ====================================================================================================================

class contactos_Post(BaseModel):
    usuario: str
    nombres: str
    apellidos: str
    correoelectronico: str
    telefono: str
    genero: str
    fechanacimiento: date
    jwtoken: str
    intentosfallidos: int
    fechabloqueo: datetime
    idrol: int
    class Config:
        orm_mode = True


class contactos_Get(contactos_Post):
    id: int


# ===============================================================================================

class estatus_Post(BaseModel):
    id_categoria: int
    descripcion: str
    class Config:
        orm_mode = True


class estatus_Get(estatus_Post):
    id: int


class mensajes_Post(BaseModel):
    id_emisor: int
    id_receptor: int
    fecha_envio: datetime
    id_estatus: int
    mensaje: str
    class Config:
        orm_mode = True


class mensajes_Get(mensajes_Post):
    id: int


class roles_Post(BaseModel):
    nombre_rol: str
    id_estatus: int
    class Config:
        orm_mode = True


class roles_Get(roles_Post):
    id: int