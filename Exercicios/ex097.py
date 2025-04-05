#!/usr/bin/env python3
def linha(txt):
    tam = len(txt)+4
    print('-'*tam)
    print(f'  {txt}')
    print('-'*tam)

linha('TÍTULO')
linha('TESTE')
linha('FRASE')
