#!/usr/bin/env python3

cores = {'limpa':'\033[m', 'vermelho': '\033[31m', 'verde': '\033[32m'} #pra facilitar a implementação de cores

n1 = int(input('Insira um valor: '))
cont = 0

for i in range(1,n1+1):
    if(n1 % i == 0):
        print('{}{}{} '.format(cores['vermelho'],i,cores['limpa']),end='')    # break removido para mostrar todos os valores divisíveis
        cont+=1
    else:
        print('{}{}{} '.format(cores['verde'],i,cores['limpa']),end='')
print('\nO número {} foi divisível {} vezes'.format(n1,cont))
if(cont==2):
    print('O número {} é primo!'.format(n1))
else:
    print('O número {} não é primo!'.format(n1))
