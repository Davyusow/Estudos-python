#!/usr/bin/env python3
from ex109 import moeda

p = float(input('Digite o preço: R$'))
moeda.resumo(p,80,20)

#print(f'A metade de R${moeda.moeda(p)} é R${(moeda.metade(p,formatar=False))}')
#print(f'O dobro de R${moeda.moeda(p)} é R${(moeda.dobro(p))}')
#print(f'Aumentando 10%, temos R${(moeda.aumentar(p,10))}')
#print(f'Reduzindo 13%, temos R${(moeda.diminuir(p,13))}')
