from rich import print


class Livro:
    nome: str
    pagina_atual: int = 0
    paginas_totais: int

    def __init__(self, nome: str, paginas: int) -> None:
        self.nome = nome
        self.paginas_totais = paginas

    def passar_pagina(self) -> None:
        self.pagina_atual += 1
        print(
            f"Livro: [bold]{self.nome}[/bold], Página: ({self.pagina_atual}/{self.paginas_totais})"
        )
        if self.pagina_atual >= self.paginas_totais:
            print("O livro foi lido completamente!")
            return


l1 = Livro("Senhor dos anéis", 10)
for i in range(10):
    l1.passar_pagina()
