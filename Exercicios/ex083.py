#!/usr/bin/env python3

expressao = str(input('Digite a expressão: '))
pilha = []
for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if(len(pilha)>0):
            pilha.pop()
        else:
            pilha.append(')')
            break
if(len(pilha) == 0):
    print('A sua expŕessão está correta')
else:
    print('A sua expressão está incorreta')
