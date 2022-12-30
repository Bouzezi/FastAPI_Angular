from fastapi import Depends,Response,APIRouter
from sqlmodel import Session
import services.crud_locataire as cl
from database import Voiture,engine,Locataire
from typing import List, Union


router = APIRouter(
    prefix="/locataires",
    tags=["locataires"],
    )


def get_session():
    with Session(engine) as session:
        yield session

@router.get("/",response_model=List[Locataire])
def locataires(session: Session = Depends(get_session)):
    return cl.all_renters(session)

@router.get("/nom/{name}",response_model=List[Locataire])
def getRenterByName(name:str,session: Session = Depends(get_session)):
    return cl.getRenterByName(name,session)

@router.get("/{id}",response_model=Union[Locataire,str])
def getRenterById(id:int,response:Response,session: Session = Depends(get_session)):
    locataire= cl.getRenterById(id,session)
    if locataire is None:
        response.status_code=404
        return "locataire non trouvée"
    return locataire

@router.post("/",response_model=Locataire,status_code=201)
def ajout_locataire(locataire:Locataire,session: Session = Depends(get_session)):
    return cl.create_Renter(locataire,session)

@router.put("/{id}",response_model=Union[Locataire,str])
def modif_locataire(modif_locataire:Locataire,id:int,response:Response,session: Session = Depends(get_session)):
    locataire=cl.update_Renter(modif_locataire,id,session)
    if locataire is None:
        response.status_code=404
        return "locataire non trouvée"
    return locataire

@router.delete("/{id}",response_model=Union[Locataire,str])
def supp_locataire(id:int,response:Response,session: Session = Depends(get_session)):
    locataire=cl.delete_Renter(id,session)
    if locataire is None:
        response.status_code=404
        return "locataire non trouvée"
    else:
        return Response(status_code=200)

