from fastapi import Response
from sqlmodel import Session, select
from database import Locataire


def all_renters(session: Session):
    stmt= select(Locataire).order_by(Locataire.nom)
    result= session.exec(stmt).all()
    return result

def getRenterById(id:int,session: Session):
    return session.get(Locataire,id)
    

def getRenterByName(name:str,session: Session):
    stmt= select(Locataire).where(Locataire.nom.like('%'+ name + '%'))
    return session.exec(stmt).all()
    

def create_Renter(locataire:Locataire,session: Session):
    session.add(locataire)
    session.commit()
    session.refresh(locataire)
    return locataire

def update_Renter(modif_locataire:Locataire,id:int,session: Session):
    locataire=getRenterById(id,session)
    if locataire:
        locataire_dict = modif_locataire.dict(exclude_unset=True)
        for key,val in locataire_dict.items():
            setattr(locataire,key,val)
        session.add(locataire)
        session.commit()
        session.refresh(locataire)
    return locataire

def delete_Renter(id:int,session: Session):
    locataire=getRenterById(id,session)
    if locataire:
        session.delete(locataire)
        session.commit()
    return locataire