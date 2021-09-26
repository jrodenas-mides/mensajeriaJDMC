from sqlalchemy import Column, ForeignKey, Integer, Boolean, String, Float, Date
from sqlalchemy.orm import relationship

from .database import Base


class Contactos(Base):
    __tablename__ = "contactos"
    Id = Column(Integer, primary_key=True, index=True)
    Usuario = Column(String, index=False, nullable=False, unique=True)
    Nombres  = Column(String, unique=False, index= True, nullable=False)
    Apellidos  = Column(String, nullable=False)
    CorreoElectronico  = Column(String, unique=True, index=True, nullable=False, )
    Telefono  = Column(Date, nullable=True)
    Genero  = Column(Date, nullable=False)
    FechaNacimiento  = Column(Date, nullable=False)
    Jwtoken  = Column(String, nullable=False)
    IntentosFallidos  = Column(Integer, nullable=False)
    FechaBloqueo  = Column(Date, nullable=False)
    IdRol  = Column(Integer, ForeignKey("roles.id") ,nullable=False)


    roles = relationship("Rol", back_populates = "contactos")
    contactos =  relationship("Amigos", back_populates = "contactos")
    estatus = relationship("Estatus", back_populates="contactos")

# ============================================================================================
class Amigos(Base):
    __tablename__ = "amigos"
    Id = Column(Integer, primary_key=True, index=True)
    Id_Contacto1 = Column(Integer, ForeignKey("contactos.id"), unique=False, index=True, nullable=False)
    Id_Contacto2 = Column(Integer,  ForeignKey("contactos.id"), unique=False, index=True, nullable=False)
    Id_Estatus = Column(Integer,  ForeignKey("estatus.id") ,nullable=False)
    Fecha_Asociacion  = Column(Date, nullable=False)
    Llave_Cifrada  = Column(String, nullable=True)

    contactos = relationship("Contactos", back_populates="amigos")
    estatus =  relationship("Estatus", back_populates="amigos")

# ====================================================================================================

class Mensajes(Base):
    __tablename__ = "mensajes"
    Id = Column(Integer, primary_key = True, index=True)
    Id_Emisor  = Column(Integer,  ForeignKey("contactos.id") , index = True)
    Id_Receptor  = Column(String,  ForeignKey("contactos.id") , index = True)
    Fecha_Envio  = Column(Date, nullable=False)
    Id_Estatus  = Column(Integer,  ForeignKey("estatus.id") ,unique=True, index=True)
    Mensaje = Column(String)


    contactos = relationship("Contactos", back_populates="mensajes")
    estatus =  relationship("Estatus", back_populates="mensajes")

# ====================================================================================================

class Estatus(Base):
    __tablename__ = "estatus"
    Id = Column(Integer, primary_key = True, index=True)
    Id_Categoria   = Column(Integer,  ForeignKey("categoriasestatus.id") ,index = True)
    Descripcion   = Column(String, index = True, unique=True)


    categoriasestatus = relationship("categoriasestatus", back_populates="estatus")

class CategoriasEstatus(Base):
    __tablename__ = "categoriasestatus"
    Id = Column(Integer, primary_key = True, index=True)
    Descripcion   = Column(String, index = True, unique=True)


class Roles(Base):
    __tablename__ = "roles"
    Id = Column(Integer, primary_key=True, index=True)
    Nombre_Rol = Column(String, index=True, unique=True)
    Id_Estatus = Column(Integer,  ForeignKey("estatus.id"))

    estatus = relationship("Estatus", back_populates="roles")