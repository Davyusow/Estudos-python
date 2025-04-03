#!/usr/bin/env python3

Pessoas = list()    #[x][0] é o nome; [x][1] é o peso
temp = list()   #usado para inserir na lista
temp.append(str(input('Nome: ')))   #[0] é o nome
temp.append(float(input('Peso: '))) #[1] é  o peso
Pessoas.append(temp[:])    #insere o temp na lista principal
temp.clear()    #limpa os dados do temp
while(True):    #Insere indefinidos números de pessoas
    prox = str(input('Deseja inserir outra pessoa?[S/N] ')).strip().upper()[0]
    if(prox == 'N'):break
    if(prox != 'S' and prox != 'N'): print('{}Opção inválida{}'.format('\033[31m','\033[m'))
    if(prox == 'S'):
        temp.append(str(input('Nome: ')))
        temp.append(int(input('Peso: ')))
        Pessoas.append(temp[:])
        temp.clear()

#Análise dos resultados:
print(f'Foram cadastradas {len(Pessoas)} pessoas')

maior = Pessoas[0][1]
for pessoa in Pessoas:  #Encontra o maior peso da lista
    if(pessoa[1]>maior): maior = pessoa[1]
print(f'O maior peso foi {maior}Kg de ',end='')
Nmaior = list() #lista que guarda o nome de todas as pessoas com o maior peso
for pessoa in Pessoas:
    if(pessoa[1]==maior): Nmaior.append(pessoa[0])
for i in range(0,len(Nmaior)): print(Nmaior[i],end=' ')
print('')

menor = Pessoas[0][1]
for pessoa in Pessoas:  #Encontra o menor peso da lista
    if(pessoa[1]<menor): menor = pessoa[1]
print(f'O menor peso foi {menor}Kg de ',end='')
Nmenor = list() #lista que guarda o nome de todas as pessoas com o menor peso
for pessoa in Pessoas:
    if(pessoa[1]==menor): Nmenor.append(pessoa[0])
for i in range(0,len(Nmenor)): print(Nmenor[i],end='')
print('')
