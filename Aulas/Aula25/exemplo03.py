from rich import print
from rich.table import Table

tabela = Table(title="Tabela de preços")

tabela.add_column("Nome")
tabela.add_column("Preço")

tabela.add_row(
    "[green]Lápis[/green]",
    "R$1.50",
)
tabela.add_row(
    "[green]Borracha[/green]",
    "R$4.50",
)

print(tabela)
