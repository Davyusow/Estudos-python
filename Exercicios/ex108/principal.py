#!/usr/bin/env python3
from ex108 import moeda

p = float(input('Digite o preço: R$'))

print(f'A metade de R${moeda.moeda(p)} é R${(moeda.metade(p))}')
print(f'O dobro de R${moeda.moeda(p)} é R${(moeda.dobro(p))}')
print(f'Aumentando 10%, temos R${(moeda.aumentar(p,10))}')
print(f'Reduzindo 13%, temos R${(moeda.diminuir(p,13))}')
