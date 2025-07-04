import datetime
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship, ForeignKey
from workout_api.generic.models import BaseModel

class TrainingCenterModel(BaseModel):
    __tablename__ = 'centros_treinamento'

    pk_id: Mapped[int] = mapped_column(Integer,primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    endereco: Mapped[str] = mapped_column(String(255), nullable=False)
    proprietario: Mapped[str] = mapped_column(String(100), nullable=False)
    atletas: Mapped[list['Atleta']] = relationship('Atleta', back_populates='centro_treinamento')
