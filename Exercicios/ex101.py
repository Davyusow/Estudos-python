#!/usr/bin/env python3
from datetime import date
def voto(ano):
    """
    →Retorna uma string da exigência do voto dependendo da idade,
    :param ano: O ano de nascimento do usuário 
    :return : retorna uma String com o resultado da exigência
    """
    resultado = ''
    idade = date.today().year - ano
    if(idade < 16):
        resultado = 'VOTO NEGADO'
    elif(idade == 16 or idade == 17 or idade > 70):
        resultado = 'VOTO OPCIONAL'
    elif(idade>=18 and idade<=70):
        resultado = 'VOTO OBRIGATÓRIO'
    return resultado


 
print('-'*30)
idade = int(input('Em que ano você nasceu? '))
print(f'Com {date.today().year - idade} anos: {voto(idade)}')
print('-'*30)
