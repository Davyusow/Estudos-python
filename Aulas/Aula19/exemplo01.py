#!/usr/bin/env python3

dados = dict()
dados = {'nome':'Pedro', 'Idade':25}
print(dados['nome'])
print(dados['Idade'])
dados['sexo'] = 'M'
print(dados['sexo'])
del dados['Idade']
print(dados)

filme = {'Título':'Star Wars',
         'Ano': 1997,
         'Diretor':'George Lucas'}
print(filme.values())
print(filme.keys())
print(filme.items())

for k,v in filme.items():
    print(f'O {k} é {v}')
locadora = []
#locadora.append(filme[:])
print(locadora[0]['Ano'])
