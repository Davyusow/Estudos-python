from rich import print
from rich.traceback import install

install()  # GOAT, mas lembrar de usar somente em depuração ou testes


def divisao(x, y) -> float:
    return x / y


print(divisao(50, 2))
print(divisao(50, 0))
