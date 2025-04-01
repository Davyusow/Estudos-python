#!/usr/bin/env python3

media = 0
hmVelho = 0
Sub20 = 0

for i in range(0,4):
    print('\n{} {}° Pessoa {}'.format('-'*5,i+1,'-'*5))
    nome = str(input('Digite o seu Nome: '))
    idade = int(input('Digite o sua idade: '))
    sexo = int(input('Digite o seu sexo:'
    '\n[ 1 ] : Masculino'
    '\n[ 2 ] : Feminino\n'))
    media+=idade
    if(sexo == 1 and idade > hmVelho): hmVelhoNome = nome
    if(sexo == 2 and idade < 20): Sub20+=1
print('A média da idade é de {}'
'\nO nome do homem mais velho é {}'
'\nE existem {} mulheres com menos de 20 anos'.format(media/4,hmVelhoNome,Sub20))
    