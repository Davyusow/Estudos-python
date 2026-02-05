from rich import print


class Funcionario:
    nome: str
    setor: str
    cargo: str
    empresa: str = "FastSoftware"

    def __init__(self, nome: str, setor: str, cargo: str) -> None:
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self) -> None:
        print(
            f"Olá :waving_hand:! sou [bold]{self.nome}[/bold], trabalho como [bold]{self.cargo}[/bold] no setor de [bold]{self.setor}[/bold] da empresa [bold]{self.empresa}[/bold]!"
        )


f1 = Funcionario("Beltrano", "Vendas", "Marketing")
f1.apresentar()
