maior = 0
menor = 1000
for i in range(0, 5):
    n1 = float(input('Digite o seu peso: '))
    if n1 > maior:
        maior = n1
    if n1 < menor:
        menor = n1
print('O maior peso foi:', maior)
print('O menor peso foi:', menor)