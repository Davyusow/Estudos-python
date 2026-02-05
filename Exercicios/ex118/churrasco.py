from turtle import width

from rich import print
from rich.panel import Panel

KILO_POR_PESSOA = 0.4
PRECO_POR_KILO = 82.40


class Churrasco:
    nome: str
    pessoas: int
    kilos: float
    preco: float

    def __init__(self, nome: str, pessoas: int) -> None:
        self.nome = nome
        self.pessoas = pessoas

    def preco_total(self) -> None:
        self.kilos = KILO_POR_PESSOA * self.pessoas
        self.preco = PRECO_POR_KILO * self.kilos

    def analisar(self) -> None:
        self.preco_total()
        texto: str = f"""
        Analisando [bold]{self.nome}[/bold] com [bold]{self.pessoas}[/bold] convidados\n
        Cada convidado comerá {KILO_POR_PESSOA:.3f}Kg e cada Kg custa R${PRECO_POR_KILO:.2f}\n
        Recomendo comprar {self.kilos:.3f}kg de carne\n
        O custo total será de R${self.preco:.2f}\n
        Cada pessoa pagará R${float(self.preco / self.pessoas):.2f} para participar.\n
        """
        print(Panel(texto, title=self.nome, width=70))


c1 = Churrasco("Churrasco dos crias", 3)
c1.analisar()
