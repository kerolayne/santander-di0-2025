from typing_extensions import Annotated
from workout_api.generic.schemas import BaseSchema
from pydantic import Field, UUID4

class TrainingCenterIn(BaseSchema):
    nome: Annotated[str, Field(description="Nome do centro de treinamento", max_length=100)]
    endereco: Annotated[str, Field(description="Endereço do centro de treinamento", max_length=255)]
    proprietario: Annotated[str, Field(description="Nome do proprietário do centro de treinamento", max_length=100)]

class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='CT King', max_length=20)]


class CentroTreinamentoOut(TrainingCenterIn):
    id: Annotated[UUID4, Field(description='Identificador do centro de treinamento')]    