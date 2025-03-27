#!/usr/bin/env python3

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
print('A média das notas do aluno é: {}'.format((n1+n2)/2))
if(media>=6.0):
    print('sua média foi boa')
else:
    print('sua média foi ruim')

print('Parábens'if media>=6.0 else 'Estuda mais!')
