from fastapi import Depends,Response,APIRouter
from sqlmodel import Session
from database import Voiture
import services.location as loc
from database import Location,engine
from typing import List, Union

router = APIRouter(
    prefix="/location",
    tags=["location"],
    )


def get_session():
    with Session(engine) as session:
        yield session

@router.post("/louer")
def louer(location:Location,response:Response,session: Session = Depends(get_session)):
    rented=loc.louer(location,session)
    if rented:
        return Response(status_code=201)
    else:
        response.status_code=500
        return "operation echouée"

@router.put("/rendre")
def rendre(location:Location,session: Session = Depends(get_session)):
    available=loc.rendre(location,session)
    if available:
        return Response(status_code=200)
    else:
        return "operation echouée"
    
@router.get("/listeVoitures/{id_loc}",response_model=Union[List[Voiture],str])
def liste_voitures_locataire(id_loc:int,response:Response,session: Session = Depends(get_session)):
    l= loc.liste_voitures_locataire(id_loc,session)
    if l == False:
        response.status_code=404
        return "locataire non trouvée"
    return l