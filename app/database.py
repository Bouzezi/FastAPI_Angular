from datetime import datetime
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel, create_engine

DATABASE_URL = "postgresql://postgres:admin@localhost:5432/locationVoiture"
engine = create_engine(DATABASE_URL, echo=True)

class Locataire(SQLModel, table=True):
    __tablename__ = 'locataire'
    id_loc: Optional[int] = Field(default=None,primary_key=True)
    nom: str =Field(index=True)
    prenom: str
    adresse: str
    voitures: List["Voiture"] = Relationship(back_populates="locataire")
    
class Voiture(SQLModel, table=True):
    # Note: Optional fields are marked as Nullable in the database
    __tablename__ = 'voiture'
    num_imma: Optional[int] = Field(default=None,primary_key=True)
    marque: str =Field(index=True)
    modele: str
    kilometrage: int
    etat: Optional[int] = Field(default=0)
    prix_location: float
    id_loc: Optional[int] = Field(default=None, foreign_key="locataire.id_loc")
    locataire: Optional[Locataire] = Relationship(back_populates="voitures")

class Location(SQLModel):
    num_imma: int
    id_loc: int


def create_tables():
    """Create the tables registered with SQLModel.metadata (i.e classes with table=True).
    More info: https://sqlmodel.tiangolo.com/tutorial/create-db-and-table/#sqlmodel-metadata
    """
    SQLModel.metadata.create_all(engine)

if __name__ == '__main__':
    # creates the table if this file is run independently, as a script
    create_tables()
