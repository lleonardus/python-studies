from db.database import Session
from db.models import Produto


class ProdutoRepository:
    def get_all(self) -> list[Produto]:
        with Session() as session:
            return session.query(Produto).all()

    def insert(self, nome: str, preco: float) -> None:
        with Session() as session:
            session.add(Produto(nome=nome, preco=preco))
            session.commit()

    def update(self, codigo: int, nome: str, preco: float) -> None:
        with Session() as session:
            session.query(Produto).filter(Produto.codigo == codigo).update(
                {Produto.nome: nome, Produto.preco: preco}, synchronize_session="fetch"
            )

            session.commit()

    def delete(self, codigo: float) -> None:
        with Session() as session:
            session.query(Produto).filter(Produto.codigo == codigo).delete()
