#!/usr/bin/env python3
try:#tenta esse bloco
    a = int(input('Digite o numerador: '))
    b = int(input('Digite o denominador: '))
    r = a / b
except Exception as erro:#se der problema faz isso
    print('{}Problema encontrao {}{}'.format('\033[31m',erro.__class__,'\033[m'))
else:#senão, prossiga #opcional
    print(f'O resultado é: {r}')
finally:#dando certo ou errado, faz isso no final #opcional
    print('Volte sempre!')