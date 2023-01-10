
from fastapi import  FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import voiture,locataire,location

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(voiture.router)
app.include_router(locataire.router)
app.include_router(location.router)