class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos
    """

    id: int
    nome: str
    saldo: float

    def __init__(self, id: int, nome: str, saldo: float) -> None:
        self.id = id
        self.nome = nome
        self.saldo = saldo
        print(f"Conta criada com sucesso! ID:{self.id}")

    def depositar(self, deposito: float) -> None:
        if deposito <= 0:
            print("Depósito com valor inválido!")
            return

        self.saldo += deposito
        print(f"Depositados R${deposito:,.2f} na conta {self.id}")

    def sacar(self, saque: float) -> None:
        if saque > self.saldo:
            print("Valor de saque não autorizado.")
            return

        self.saldo -= saque
        print(f"Sacado R${saque:,.2f} da conta {self.id}")

    def __str__(self) -> str:
        return f"ID: {self.id}\nNome: {self.nome}\nSaldo: {self.saldo:,.2f}"
