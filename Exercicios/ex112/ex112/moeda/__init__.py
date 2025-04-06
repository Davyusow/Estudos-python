#!/usr/bin/env python3
def metade(m,formatar=True):
    resultado = m/2
    if(formatar):
        return f'{resultado:.2f}'.replace('.',',')
    else:return resultado

def dobro(m,formatar=True):
    resultado = m*2
    if(formatar):
        return f'{resultado:.2f}'.replace('.',',')
    else:return resultado

def aumentar(m,p,formatar=True):
    resultado = m * (1 + (p/100))
    if(formatar):
        return f'{resultado:.2f}'.replace('.',',')
    else:return resultado

def diminuir(m,p,formatar=True):
    resultado = m - (m * (p/100))
    if(formatar):
        return f'{resultado:.2f}'.replace('.',',')
    else:return resultado

def moeda(p,formatar=True):
    if(formatar):
        return f'{p:.2f}'.replace('.',',')
    else: return p

def resumo(P,A,R):
    print(f'{"-"*30}\n{"Resumo":^30}\n{"-"*30}')
    print(f'{"Preço Analisado:":<20}R${moeda(P,formatar=True)}')
    print(f'{"Dobro do Preço:":<20}R${dobro(P,formatar=True)}')
    print(f'{"Metade do Preço:":<20}R${metade(P,formatar=True)}')
    print('Aumento de {:<9}R${}'.format(str(f'{A}%:'),aumentar(P,A,formatar=True)))
    print('Redução de {:<9}R${}'.format(str(f'{R}%:'),diminuir(P,R,formatar=True)))
    print('-'*30)
