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
    Jwtoken: str
    IntentosFallidos: int
    FechaBloqueo: datetime
    IdRol: int
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
    Id_Emisor: int
    Id_Receptor: int
    Fecha_Envio: datetime
    Id_Estatus: int
    Mensaje: str
    class Config:
        orm_mode = True


class mensajes_Get(mensajes_Post):
    id: int


class roles_Post(BaseModel):
    nombre_rol: str
    Id_Estatus: int
    class Config:
        orm_mode = True


class roles_Get(roles_Post):
    id: int