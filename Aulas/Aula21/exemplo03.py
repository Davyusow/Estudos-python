#!/usr/bin/env python3
def somar(a=0,b=0,c=0): #a=0 transforam o a em um parâmetro opcional
    """
    → Faz a soma de três valores e mostra o resultado na tela.
    :param a: O primeiro valor
    :param b: O segundo valor
    :param c: O terceiro valor
    :return : sem retorno
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(3,2,5)
somar(8,4)
somar(1)
somar()
