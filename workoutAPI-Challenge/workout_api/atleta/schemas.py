from pydantic import BaseModel

class Atleta(BaseModel):
    id: int
    nome: str
    idade: int
    peso: float
    altura: float