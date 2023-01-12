from fastapi import Depends, HTTPException,Response,APIRouter
from sqlmodel import Session
import services.crud_voiture as cv
from database import Voiture,engine
from typing import List, Union


router = APIRouter(
    prefix="/voitures",
    tags=["voitures"],
    )


def get_session():
    with Session(engine) as session:
        yield session
        

@router.get("/",response_model=List[Voiture])
def voitures(session: Session = Depends(get_session)):
    return cv.all_cars(session)

@router.get("/disponible",response_model=List[Voiture])
def voituresDisponible(session: Session = Depends(get_session)):
    return cv.all_cars_not_rented(session)

@router.get("/louee",response_model=List[Voiture])
def voituresDisponible(session: Session = Depends(get_session)):
    return cv.all_cars_rented(session)

@router.get("/nombre")
def nombreVoitures(session: Session = Depends(get_session)):
    return cv.total_number_cars(session)

@router.get("/kilometrage moyenne")
def kilometrageMoyenne(session: Session = Depends(get_session)):
    return cv.average_kilo_cars(session)

@router.get("/{num_imma}",response_model=Union[Voiture,str])
def voiture(num_imma:int,response:Response,session: Session = Depends(get_session)):
    voiture=cv.getCarByNum(num_imma,session)
    if voiture is None:
        response.status_code=404
        return "voiture non trouvée"
    return voiture 

@router.get("/marque/{brand}",response_model=List[Voiture])
def getCarByBrand(brand:str,session: Session = Depends(get_session)):
    return cv.getCarByBrand(brand,session)

@router.post("/",response_model=Union[Voiture,str],status_code=201)
def ajout_voiture(voiture:Voiture,session: Session = Depends(get_session)):
    return cv.create_car(voiture,session)

@router.put("/{num_imma}",response_model=Union[Voiture,str])
def modif_voiture(modif_voiture:Voiture,num_imma:int,response:Response,session: Session = Depends(get_session)):
    voiture =cv.update_car(modif_voiture,num_imma,session)
    if voiture is None:
        response.status_code=404
        return "voiture non trouvée"
    return voiture

@router.delete("/{num_imma}")
def supp_voiture(num_imma:int,response:Response,session: Session = Depends(get_session)):
    voiture= cv.delete_car(num_imma,session)
    if voiture is None:
        response.status_code=404
        return "voiture non trouvée"
    else:
        return Response(status_code=200)

