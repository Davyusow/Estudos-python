#!/usr/bin/env python3
def teste():
    print(f'Na função teste, o n vale {n}')
    x = 8   #variável local
    print(f'Na função teste, o x vale {x}')

#Programa Principal
n=2 #variável global
print(f'No programa principal, n vale {n}')
teste()
#print(f'No programa principal a função vale {x}')  #x não existe globalmente, logo ocorre um erro
