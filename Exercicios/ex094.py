#!/usr/bin/env python3

Pessoas = []; cadastrado = {}
#primeiro cadastro
print('-'*50)
cadastrado['Nome'] = str(input('Nome: '))
while(True):
    cadastrado['Sexo'] = str(input('Sexo[M/F]: ')).strip().upper()[0]
    if(cadastrado['Sexo'] != 'F' and cadastrado['Sexo'] != 'M'):
        print('{}Opção inválida!{}'.format('\033[31m','\033[m'))
    else:break
cadastrado['Idade'] = int(input('Idade: '))        
Pessoas.append(cadastrado.copy())
media = cadastrado['Idade']

cadastrado.clear()

#looping com as outras pessoas
while(True):
    print('-'*50)
    prox = str(input('Deseja inserir outro?[S/N]: ')).strip().upper()[0]
    if(prox != 'S' and prox != 'N'):
        print('{}Opção inválida!{}'.format('\033[31m','\033[m'))
    elif(prox == 'N'):break
    elif(prox == 'S'):
        cadastrado['Nome'] = str(input('Nome: '))
        while(True):
            cadastrado['Sexo'] = str(input('Sexo[M/F]: ')).strip().upper()[0]
            if(cadastrado['Sexo'] != 'F' and cadastrado['Sexo'] != 'M'):
                print('{}Opção inválida!{}'.format('\033[31m','\033[m'))
            else:break
        cadastrado['Idade'] = int(input('Idade: '))        
        Pessoas.append(cadastrado.copy())
        media += cadastrado['Idade']
        cadastrado.clear()
#análise de dados
print('-'*50)
media /= len(Pessoas)
print(f'Foram cadastradas {len(Pessoas)} pessoas')
print(f'A Média de idade do grupo é de {media:.1f}')
print('-'*50)
print('A lista de mulheres no grupo é: ')
for i in Pessoas:
    if(i['Sexo'] == 'F'): print(i['Nome'])
print('-'*50)
print('A lista de pessoas com idade acima da média é: ')
for i in Pessoas:
    if(i['Idade'] > media): print(f'Nome: {i["Nome"]}; Sexo: {i["Sexo"]};Idade: {i["Idade"]}')
print('-'*50)
