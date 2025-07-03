import datetime
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship, ForeignKey
from workout_api.generic.models import BaseModel

class CategoriesModel(BaseModel):
    __tablename__ = 'categorias'

    pk_id: Mapped[int] = mapped_column(Integer,primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    atleta: Mapped['AtletaModel'] = relationship('AtletaModel', back_populates='categoria')
