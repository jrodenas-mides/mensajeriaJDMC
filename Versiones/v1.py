from fastapi import FastAPI
from Routers import Amigos, Contacto, Mensaje

app_v1 = FastAPI(root_path="/auth")

tags_metadata = [
    {"name": "Amigos", "description": "Servicios para administrar los amigos"},
    {"name": "Contacto", "description": "Servicios para administrar los contactos"},
    {"name": "Mensaje", "description": "Servicios para administrar los mensajes"}
]

app_v1 = FastAPI(root_path="/v1", openapi_tags=tags_metadata)
app_v1.include_router(Amigos.router)
app_v1.include_router(Contacto.router)
app_v1.include_router(Mensaje.router)

