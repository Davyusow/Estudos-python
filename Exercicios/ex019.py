#!/usr/bin/env python3
from random import randint,choice

nome1 = str(input('Primeiro aluno: '))
nome2 = str(input('Segundo aluno: '))
nome3 = str(input('terceiro aluno: '))
nome4 = str(input('Quarto aluno: '))
sorteio = randint(1,4)
lista = [nome1,nome2,nome3,nome4]
#sorteio = choice(lista) 
#O método choice escolhe um indíce da lista
#E retorna o valor deste índice da lista, então para usar ele seria
#Apenas necessário imprimir o prórpio sorteio
print('O aluno escolhido foi {}'.format(lista[sorteio]))
