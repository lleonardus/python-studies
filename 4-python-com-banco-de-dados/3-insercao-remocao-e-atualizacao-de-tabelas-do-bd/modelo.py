class Pessoa:
    def __init__(
        self,
        cpf: int,
        nome: str,
        nascimento: str,
        oculos: bool,
    ) -> None:
        self.cpf = cpf
        self.nome = nome
        self.nascimento = nascimento
        self.oculos = oculos
        self.veiculos = []


class Marca:
    def __init__(self, id: int | None, nome: str, sigla: str) -> None:
        self.id = id
        self.nome = nome
        self.sigla = sigla


class Veiculo:
    def __init__(
        self,
        placa: str,
        ano: int,
        motor: float,
        cor: str,
        proprietario: int,
        marca: int | None,
    ) -> None:
        self.placa = placa
        self.ano = ano
        self.motor = motor
        self.cor = cor
        self.proprietario = proprietario
        self.marca = marca
