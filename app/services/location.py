from sqlmodel import Session
from database import Location
from services.crud_voiture import getCarByNum
from services.crud_locataire import getRenterById

def louer(location:Location,session:Session):
    voiture=getCarByNum(location.num_imma,session)
    locataire=getRenterById(location.id_loc,session)
    if voiture and locataire:
        locataire.voitures.append(voiture)
        voiture.etat=1
        session.add(locataire)
        session.commit()
        session.refresh(locataire)
        return True
    else:
        return False

def rendre(location:Location,session:Session):
    voiture=getCarByNum(location.num_imma,session)
    if voiture:
        voiture.locataire = None
        voiture.etat=0
        session.add(voiture)
        session.commit()
        session.refresh(voiture)
        return True
    else:
        return False

def liste_voitures_locataire(id_loc:int,session:Session):
    locataire=getRenterById(id_loc,session)
    if locataire:
        return locataire.voitures
