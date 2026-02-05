from conta import ContaBancaria

c1 = ContaBancaria(112, "Beltrano", 3_000)
print(c1)

print("\nSacando R$15.000.000,00!")
c1.sacar(15_000_000.00)
print(c1)

print("\nDepositando -R$200.00!")
c1.depositar(-200.00)
print(c1)
