from sqlalchemy import Column, ForeignKey, Integer, Boolean, String, Float, Date
from sqlalchemy.orm import relationship

from .database import Base


class Contactos(Base):
    __tablename__ = "contactos"
    id = Column(Integer, primary_key=True, index=True)
    usuario = Column(String, index=False, nullable=False, unique=True)
    nombres  = Column(String, unique=False, index= True, nullable=False)
    apellidos  = Column(String, nullable=False)
    correoelectronico  = Column(String, unique=True, index=True, nullable=False, )
    telefono  = Column(Date, nullable=True)
    genero  = Column(Date, nullable=False)
    fechanacimiento  = Column(Date, nullable=False)
    jwtoken  = Column(String, nullable=False)
    intentosfallidos  = Column(Integer, nullable=False)
    fechabloqueo  = Column(Date, nullable=False)
    idrol = Column(Integer, ForeignKey("roles.id") ,nullable=False)


    roles = relationship("Roles", back_populates = "contactos")
    amigos =  relationship("Amigos", back_populates = "contactos")
    mensajes = relationship("Mensajes", back_populates="contactos")

# ============================================================================================
class Amigos(Base):
    __tablename__ = "amigos"
    id = Column(Integer, primary_key=True, index=True)
    id_contacto1 = Column(Integer, ForeignKey("contactos.id"), unique=False, index=True, nullable=False)
    id_contacto2 = Column(Integer, unique=False, index=True, nullable=False)
    id_estatus = Column(Integer,  ForeignKey("estatus.id") ,nullable=False)
    fecha_asociacion  = Column(Date, nullable=False)
    llave_cifrada  = Column(String, nullable=True)

    contactos = relationship("Contactos", back_populates="amigos")
    estatus =  relationship("Estatus", back_populates="amigos")

# ====================================================================================================

class Mensajes(Base):
    __tablename__ = "mensajes"
    id = Column(Integer, primary_key = True, index=True)
    id_Emisor  = Column(Integer,  ForeignKey("contactos.id") , index = True)
    id_Receptor  = Column(String , index = True)
    fecha_envio  = Column(Date, nullable=False)
    id_estatus  = Column(Integer,  ForeignKey("estatus.id") ,unique=True, index=True)
    mensaje = Column(String)


    contactos = relationship("Contactos", back_populates="mensajes")
    estatus =  relationship("Estatus", back_populates="mensajes")

# ====================================================================================================

class Estatus(Base):
    __tablename__ = "estatus"
    id = Column(Integer, primary_key = True, index=True)
    id_Categoria   = Column(Integer,  ForeignKey("categoriasestatus.id") ,index = True)
    descripcion   = Column(String, index = True, unique=True)


    categoriasestatus = relationship("CategoriasEstatus", back_populates="estatus")
    amigos = relationship("Amigos", back_populates="estatus")
    mensajes = relationship("Mensajes", back_populates="estatus")
    roles = relationship("Roles", back_populates="estatus")


class CategoriasEstatus(Base):
    __tablename__ = "categoriasestatus"
    id = Column(Integer, primary_key = True, index=True)
    descripcion   = Column(String, index = True, unique=True)

    estatus = relationship("Estatus", back_populates="categoriasestatus")

class Roles(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True)
    nombre_rol = Column(String, index=True, unique=True)
    id_estatus = Column(Integer,  ForeignKey("estatus.id"))

    estatus = relationship("Estatus", back_populates="roles")
    contactos = relationship("Contactos", back_populates="roles")