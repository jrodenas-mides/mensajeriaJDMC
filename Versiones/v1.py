from fastapi import FastAPI
from Routers import Amigos

app_v1 = FastAPI()

tags_metadata = [
    {"name": "Amigos", "description": "Servicios para administrar los amigos"}
]

app_v1 = FastAPI(root_path="/v1", openapi_tags=tags_metadata)
app_v1.include_router(Amigos.router)

