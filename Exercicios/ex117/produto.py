from rich import print
from rich.panel import Panel


class Produto:
    nome: str
    preco: float

    def __init__(self, nome: str, preco: float) -> None:
        self.nome = nome
        self.preco = preco

    def mostrar_etiqueta(self) -> None:
        print(Panel(f"{self.preco:,.2f}", title=self.nome))


p1 = Produto("Café", 14.99)
p2 = Produto("Motorola G2", 800.00)

p1.mostrar_etiqueta()
p2.mostrar_etiqueta()
