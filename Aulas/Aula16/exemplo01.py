#!/usr/bin/env python3

lanche = ('Hambúrguer','Suco','Pizza','Pudim','Batata Frita')
print(lanche[-2]) #-1 imprime o último índice, e o -2 o penúltimo índice
print(lanche[1])
# lanche[1] = 'Refrigerante' #alterar o valor de uma tupla é impossível
print(len(lanche))

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

for i in range(0,len(lanche)):
    print(f'Vou comer {i+1}° a(o) {lanche[i]}')

for i,comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {i+1}')

print(sorted(lanche))

a = (2,5,4)
b = (5,8,1,2)
print(a)
print(b)
c = a + b
print(c)
print(c.count(5))
print(c.index(8))
print(c.index(2))
pessoa = ('Gustavo',39,'M',99.88)
print(pessoa)
del(pessoa)
print(pessoa)
