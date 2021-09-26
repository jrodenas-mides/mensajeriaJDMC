from fastapi import FastAPI
from Versiones.v1 import app_v1


#Proyecto Final
app = FastAPI()

app.mount("/v1", app_v1)

@app.get("/version")
async def version():
    curso = 'Python'  # Cadena de Caracteres
    version = 1  # Valores Enteros
    subVersion = 0.5  # Valores de coma flotante
    habilitado = True  # Valores Booleanos (True / False)
    lastUpdated = '2021-09-23'

    version = str(version) + '.' + str(subVersion)

    return {'curso': curso,
            'version': version,
            'subversion': subVersion,
            'habilitado': habilitado,
            'actualizada': lastUpdated
            }