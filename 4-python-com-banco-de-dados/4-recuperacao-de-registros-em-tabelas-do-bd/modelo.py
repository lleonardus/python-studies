from dataclasses import dataclass
from datetime import date


@dataclass
class Pessoa:
    cpf: int
    nome: str
    nascimento: str | date
    oculos: bool


@dataclass
class Marca:
    id: int | None
    nome: str
    sigla: str


@dataclass
class Veiculo:
    placa: str
    ano: int
    motor: float
    cor: str
    proprietario: int
    marca: Marca | int | None
