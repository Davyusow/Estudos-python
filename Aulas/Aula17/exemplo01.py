#!/usr/bin/env python3

num = [2,5,9,1] #declaração da lista
print(num)
num[2] = 3  #troca o valor da lista em um índice
print(num)
num.append(7)   #insere o valor no fim da lista
print(num)
num.sort() ; print(num) #sort organiza em ordem alfabética ou em ordem numérica crescente
num.sort(reverse=True) ; print(num) #inverte a ordem do sort
num.insert(2,0); print(num) #insert insere o no índice (primeiro argumento) o valor do segundo argumento

print(f'Essa Lista tem {len(num)} elementos')
num.pop() ; print(num)  #o pop remove o último valor da lista
num.pop(2) ; print(num)  #remove o valor do indíce 2
num.insert(2,2) ; print(num)
num.remove(2) ; print(num) #remove() remove o primeiro valor 2 da lista

if(4 in num):
    num.remove(4)
else:
    print('Não encontrei o valor 4')
print(num)
