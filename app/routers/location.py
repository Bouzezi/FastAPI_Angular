from fastapi import Depends,Response,APIRouter
from sqlmodel import Session
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
def louer(location:Location,session: Session = Depends(get_session)):
    rented=loc.louer(location,session)
    if rented:
        return Response(status_code=201)
    else:
        return "operation echouée"

@router.put("/rendre")
def louer(num:int,session: Session = Depends(get_session)):
    available=loc.rendre(num,session)
    if available:
        return Response(status_code=200)
    else:
        return "operation echouée"