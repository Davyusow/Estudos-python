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
print(f'Foram Digitados {len(n1)} números')
print(f'A lista em ordem Decrescente é:')
n1.sort(reverse=True)
print(n1)
if(5 in n1): print('O 5 está presente na lista')
else: print('O 5 não está na lista')
