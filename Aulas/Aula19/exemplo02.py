#!/usr/bin/env python3

pessoas = {'Nome':'Gustavo','Sexo':'M','Idade':22}
print(f'O {pessoas["Nome"]}')
print(pessoas.keys())
print(pessoas.values())

for k,v in pessoas.items():
    print(f'{k} = {v}')
brasil = []
estado1 = {'Uf': 'Rio de janeiro','Sigla':'RJ'}
estado2 = {'Uf': 'São Paulo','Sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0])
