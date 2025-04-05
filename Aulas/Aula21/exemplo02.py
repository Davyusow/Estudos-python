#!/usr/bin/env python3
def contador(i,f,p):
    """
    →Faz uma contagem e mostra na tela,
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """#é o docstring da função, ao usar a função contador como parâmentro
       #da função help(), este texto entre as 3 aspas duplas será retornado
    c=i
    while(c<=f):
        print(f'{c}',end='..')
        c += p
    print('FIM!')


help(contador)
contador(2,10,2)
