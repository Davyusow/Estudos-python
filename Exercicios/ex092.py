#!/usr/bin/env python3
from datetime import date
Pessoa = {}
Pessoa['Nome'] = str(input('Nome: '))
Pessoa['Idade'] = date.today().year - int(input('Ano  de Nascimento: '))
Pessoa['Ctps'] = int(input('Carteira de trabalho(0 não tem): '))
if(Pessoa['Ctps'] != 0):
    Pessoa['AnoDeContratação'] = int(input('Ano de Contratação: '))
    Pessoa['Salário'] = float(input('Salário: R$'))
print(Pessoa)
print(f'O nome tem valor {Pessoa["Nome"]}')
print(f'A idade tem valor {Pessoa["Idade"]}')
print(f'O Ctps tem o valor: {Pessoa["Ctps"]}')
if(Pessoa['Ctps'] != 0):
    print(f'O salário tem valor: {Pessoa["Salário"]}')
    Pessoa["aposentadoria"] = (Pessoa['AnoDeContratação'] - date.today().year)+Pessoa['Idade'] + 35 #idade na contratação
    print(f'Aposentadoria tem o valor: {Pessoa["aposentadoria"]}')#aposentadoria = 35 anos de contribuição
