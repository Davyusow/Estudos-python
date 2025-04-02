#!/usr/bin/env python3

numeros = ('Zero','Um','Dois','Três','Quatro','Cinco,',
'Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze',
'Quatorze','Quize','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')


n1 = int(input('Insira o número: '))

while(n1 < 0 or n1 > 20):
    n1 = int(input('{}Valor Inválido!{}'
    '\nInsira o número: '.format('\033[31m','\033[m')))
print(f'O número digitado foi {numeros[n1]}')
