from sqlmodel import Session, select,func
from database import Voiture



def all_cars(session: Session):
    stmt= select(Voiture)
    result= session.exec(stmt).all()
    return result

def all_cars_not_rented(session: Session):
    stmt= select(Voiture).where(Voiture.etat == 0)
    result= session.exec(stmt).all()
    return result

def getCarByNum(num_imma:int,session: Session):
    return session.get(Voiture,num_imma)

def total_number_cars(session: Session):
    stmt=select([func.count(Voiture.num_imma)])
    return session.exec(stmt).first()

def average_kilo_cars(session: Session):
    stmt=select([func.avg(Voiture.kilometrage)])
    return session.exec(stmt).first()

def create_car(voiture:Voiture,session: Session):
    session.add(voiture)
    session.commit()
    session.refresh(voiture)
    return voiture

def update_car(modif_voiture:Voiture,num_imma:int ,session: Session):
    voiture=getCarByNum(num_imma,session)
    if voiture:
        voiture_dict = modif_voiture.dict(exclude_unset=True)
        for key,val in voiture_dict.items():
            setattr(voiture,key,val)
        session.add(voiture)
        session.commit()
        session.refresh(voiture)
    return voiture

def delete_car(num_imma:int,session: Session):
    voiture=voiture=getCarByNum(num_imma,session)
    if voiture:
        session.delete(voiture)
        session.commit()
    return voiture
    