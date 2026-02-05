class Garfanhoto:
    """
    Classe que faz um garfanhoto/aluno
    """

    nome: str
    idade: int

    def __init__(self, nome: str = "", idade: int = 0) -> None:
        self.nome = nome
        self.idade = idade

    def aniversario(self) -> None:
        self.idade += 1

    def __str__(self) -> str:
        return f"Garfanhoto:\nNome: {self.nome}\nIdade: {self.idade}"


g1 = Garfanhoto("Davyusow", 21)

print(g1)
g1.aniversario()
print(g1)

print("g2:")
g2 = Garfanhoto("Beltrana", 23)

print(g2)
print(g2.__dict__)  # atributo
# Woow um json!!
print(g2.__getstate__())  # método
print(g2.__class__)


print(Garfanhoto.__doc__)
