#!/usr/bin/env python3
def fatorial(num=1):
    f = 1
    for contador in range(num,0,-1):
        f *= contador
    return f


n1 = int(input('Digite um número: '))
print(f'fatorial de {n1} é igual à: {fatorial(n1)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()

print(f'Os resultados foram {f1}, {f2} e {f3}')

