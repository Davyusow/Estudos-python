#!/usr/bin/env python3

while(True):    #while infinito
    print('teste')
    break   #para a execução do laço

cont = 1
while(cont<=10):
    print(cont,end=' ')
    cont += 1
print('Acabou')
s = 0
while(True):
    n1 = int(input('Digite um número: '))
    if(n1 == 999): break
    s+=n1
print('A soma dos valores vale {}'.format(s))
print(f'A soma vale {s}')   #nova forma de usar print
nome = 'José'
idade = 33
print(f'O {nome} tem {idade} anos')
salário = 987.35
print(f'O {nome:-^20} tem {idade:<20} anos e ganha R${salário:.2f}')
