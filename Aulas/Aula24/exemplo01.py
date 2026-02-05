class Garfanhoto:
    nome: str
    idade: int

    def __init__(self, nome: str = "", idade: int = 0) -> None:
        self.nome = ""
        self.idade = 0

    def aniversario(self) -> None:
        self.idade += 1

    def mensagem(self) -> str:
        return f"{self.nome} é um aluno e tem {self.idade}"


g1 = Garfanhoto()
g1.nome = "Davyusow"
g1.idade = 21

print(g1.mensagem())
g1.aniversario()
print(g1.mensagem())

g2 = Garfanhoto()
g2.nome = "Beltrana"
g2.idade = 23

print(g2)
print(f"Nome: {g2.nome}")
print(f"Idade: {g2.idade}")
