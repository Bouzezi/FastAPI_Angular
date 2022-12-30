
from fastapi import  FastAPI
from routers import voiture,locataire,location
app = FastAPI()

app.include_router(voiture.router)
app.include_router(locataire.router)
app.include_router(location.router)