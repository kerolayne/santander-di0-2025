from typing_extensions import Annotated
from workout_api.generic.schemas import BaseSchema
from pydantic import Field

class TrainingCenter(BaseSchema):
    nome: Annotated[str, Field(description="Nome do centro de treinamento", max_length=100)]
    endereco: Annotated[str, Field(description="Endereço do centro de treinamento", max_length=255)]
    proprietario: Annotated[str, Field(description="Nome do proprietário do centro de treinamento", max_length=100)]
