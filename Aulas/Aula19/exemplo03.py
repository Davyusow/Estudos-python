#!/usr/bin/env python3
estado = {}
brasil = []
for i in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k,v in e.items():
        print(f'O campo {k} tem o valor {v}')

for e in brasil:
    for v in e.values():
        print(f'{v}')
        