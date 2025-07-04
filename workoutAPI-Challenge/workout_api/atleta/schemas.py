from pydantic import BaseModel, Field, UUID4, OutMixin
from typing import Annotated, Optional
from workout_api.generic.schemas import BaseSchema
from workout_api.training_center.schemas import CentroTreinamentoAtleta
from workout_api.categories.schemas import CategoriaIn

class Atleta(BaseSchema):
    id: int
    nome: Annotated[str, Field(description="Nome do atleta", max_length=100)]
    cpf: Annotated[str, Field(description="CPF do atleta", regex=r"^\d{11}$")]
    idade: Annotated[int, Field(description="Idade do atleta", ge=0)]
    peso: Annotated[float, Field(description="Peso do atleta", gt=0)]
    altura: Annotated[float, Field(description="Altura do atleta", gt=0)]
    sexo: Annotated[str, Field(description="Sexo do atleta", max_length=1, regex=r"^[MF]$")]
    categoria: Annotated[CategoriaIn, Field(description='Categoria do atleta')]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description='Centro de treinamento do atleta')]


class AtletaIn(Atleta):
    pass


class AtletaOut(Atleta, OutMixin):
    pass

class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(None, description='Nome do atleta', example='Joao', max_length=50)]
    idade: Annotated[Optional[int], Field(None, description='Idade do atleta', example=25)]
