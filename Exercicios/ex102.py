#!/usr/bin/env python3
def fatorial(n,show=False):
    """
    →Retorna o valor do fatorial
    :param n: valor à ser fatorado
    :param show: Parâmetro para permitir ou não o retorno de todo o cálculo
    :return : Retorna o inteiro com o resultado
    """
    f = 1
    resultado = ''
    for i in range(n,0,-1):
        f *= i
        if(show and i!=1):
            resultado += f'{i} x '
        elif(show and i==1):
            resultado += f'{i} = '
    if(show): print(resultado,end='') ;return f
    else: return f


print(fatorial(5,show=True))
print(fatorial(5))
