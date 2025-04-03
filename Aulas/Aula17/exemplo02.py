#!/usr/bin/env python3

valores = []
for cont in range(0,10):
    valores.append(int(input(f"Inira o {cont+1}° valor: ")))

for i in valores:
    print(f'{i}...',end='')
print()

for i,v in enumerate(valores):
    print(f'Na posição {i+1}, encontrei o valor {v}...')
print('Cheguei ao final da lista')
