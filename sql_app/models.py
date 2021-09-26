from sqlalchemy import Column, ForeignKey, Integer, Boolean, String, Float, Date
from sqlalchemy.orm import relationship

from .database import Base


class Autor(Base):
    __tablename__ = "autor"
    id = Column(Integer, primary_key=True, index=True)
    usuario = Column(String, unique=False, index=False)
    apellido = Column(String, unique=False, index= True)
    nacimiento = Column(Date, nullable=False)
    pais = Column(String, unique=False, index=True, nullable=False)
    fallecimiento = Column(Date, nullable=True)

    libros = relationship("Libro", back_populates = "autor")


# ============================================================================================
class Categoria(Base):
    __tablename__ = "categoria"
    id = Column(Integer, primary_key=True, index=True) # Higher Order Functions: Funcions que reciben una function como parametro y devuelven otra función como parametro
    nombre = Column(String, unique=True, index=True)
    libros = relationship("Libro", back_populates="categoria")

# ====================================================================================================

class Editorial(Base):
    __tablename__ = "editorial"
    id = Column(Integer, primary_key = True, index=True)
    nombre = Column(String, unique = True, index = True)
    pais = Column(String)

    libros = relationship("Libro", back_populates="editorial")

# ====================================================================================================

class Libro(Base):
    __tablename__ = "libro"
    id = Column(Integer, primary_key= True, index = True)
    nombre = Column(String, unique= True, index = True)
    id_autor = Column(Integer, ForeignKey("autor.id"), index=True)
    id_categoria = Column(Integer, ForeignKey("categoria.id"), index=True)
    precio = Column(Float, nullable=False)
    edicion = Column(String, nullable=True)
    id_editorial = Column(Integer, ForeignKey("editorial.id"), index=True)
    anio_impresion = Column(Integer, nullable=False)

    autor = relationship("Autor", back_populates="libros")
    categoria = relationship("Categoria", back_populates="libros")
    editorial = relationship("Editorial", back_populates="libros")


# ==========================================================================================================

class Cliente(Base):
    __tablename__ = "cliente"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apellidos = Column(String, nullable=False, index=True)
    correo = Column(String, nullable=False, unique=True, index=True)

