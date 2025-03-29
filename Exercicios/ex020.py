#!/usr/bin/env python3

#!/usr/bin/env python3
from random import randint,shuffle

nome1 = str(input('Primeiro aluno: '))
nome2 = str(input('Segundo aluno: '))
nome3 = str(input('terceiro aluno: '))
nome4 = str(input('Quarto aluno: '))
sorteio = randint(1,4)
lista = [nome1,nome2,nome3,nome4]
print('A ordem de apresentação será: ')
shuffle(lista) #o random.shuffle embaralha a lista aleatoriamente
print('{}, {}, {} e {}'.format(lista[0],lista[1],lista[2],lista[3]))


