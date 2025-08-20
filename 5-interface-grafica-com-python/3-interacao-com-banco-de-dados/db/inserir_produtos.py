from faker import Faker
from repository.produto_repository import ProdutoRepository

fake = Faker("pt_BR")
repository = ProdutoRepository()

for _ in range(10):
    repository.insert(
        nome=fake.word(), preco=round(fake.random_number(digits=5) / 100, 2)
    )


print("Dados inseridos com sucesso!")
