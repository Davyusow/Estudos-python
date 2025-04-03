#!/usr/bin/env python3
n1 = list()
n1.append(int(input('Insira um número na lista: ')))
while(True):
    teste = str(input('Deseja inserir outro número?[S/N] ')).strip().upper()[0]
    if(teste == 'S'):
        n1.append(int(input('Insira um número na lista: ')))
    elif(teste == 'N'):
        break
    else:
        print('{}Opção inválida!{}'.format('\033[31m','\033[m'))
impar = list() ;par = list()
for i in range(0,len(n1)):
    if(n1[i] % 2 == 0):
        par.append(n1[i])
    elif(n1[i] % 2 == 1):
        impar.append(n1[i])
print('Lista com todos os números: ');print(n1)
print('Lista dos números par: ');print(par)
print('Lista dos números ímpar: ');print(impar)
