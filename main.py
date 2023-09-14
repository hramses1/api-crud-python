from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.MainRoutes import main

app = FastAPI(
    title="CRUD USUARIO",
    description="API PARA AGREGAR USUARIOS",
    version="0.0.1",
    debug=True
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(main)