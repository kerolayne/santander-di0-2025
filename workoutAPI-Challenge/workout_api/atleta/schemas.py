from pydantic import BaseModel, Field
from typing import Annotated
from workout_api.generic.schemas import BaseSchema

class Atleta(BaseSchema):
    id: int
    nome: Annotated[str, Field(description="Nome do atleta", max_length=100)]
    cpf: Annotated[str, Field(description="CPF do atleta", regex=r"^\d{11}$")]
    idade: Annotated[int, Field(description="Idade do atleta", ge=0)]
    peso: Annotated[float, Field(description="Peso do atleta", gt=0)]
    altura: Annotated[float, Field(description="Altura do atleta", gt=0)]
    sexo: Annotated[str, Field(description="Sexo do atleta", max_length=1, regex=r"^[MF]$")]

