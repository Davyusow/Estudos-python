from rich import print
from rich.panel import Panel
from rich.traceback import install

install()


class Gamer:
    nome: str
    nick: str
    jogos_favoritos: list[str]

    def __init__(self, nome: str, nick: str) -> None:
        self.nome = nome
        self.nick = nick
        self.jogos_favoritos = []

    def add_favoritos(self, game: str) -> None:
        if game in self.jogos_favoritos:
            print(f"O jogo [bold]{game}[/bold] já esta favoritado!")
        self.jogos_favoritos.append(game)

    def mostrar_favoritos(self) -> str:
        texto: str = ""

        for jogo in self.jogos_favoritos:
            if jogo is not None:
                texto += ":video_game:" + jogo + "\n\t"
        return texto

    def ficha(self) -> None:
        texto: str = f"""
        Nome real: [cyan bold]{self.nome}[/cyan bold]
        Jogos Favoritos:
        [magenta]{self.mostrar_favoritos()}[/magenta]
        """

        print(Panel(texto, title=f"Jogador: {self.nick}", width=70))


g1 = Gamer("Dayvson Farias", "davyusow")

g1.add_favoritos("Dark Souls")
g1.add_favoritos("Metal Gear")

g1.ficha()
