#!/usr/bin/env python3
def Titulo(txt,cor="Limpa"):
    texto = {'Branco':'\033[1;30;47m','Vermelho':'\033[7;31;47m',
             'Verde':'\033[1;32m','Amarelo':'\033[1;33;47m',
             'Azul':'\033[1;34;47m','Roxo':'\033[1;35;47m',
             'Ciano':'\033[7;36;47m','Cinza':'\033[1;37m',
             'Limpa':'\033[m'}
    tam = len(txt)+4
    print(f'{texto[cor]}{"-"*tam}\n  {txt}  \n{"-"*tam}{texto["Limpa"]}',flush=True)

def Ajuda():
    from time import sleep
    Titulo('Sistema de Ajuda PyHelp',cor="Ciano")
    while(True):
        busca = str(input('Função ou biblioteca > '))
        if(busca.upper() == 'FIM'): Titulo('Até logo!',cor="Vermelho");break
        Titulo(f'Acessando Manual do comando {busca}',"Verde")
        sleep(1)
        help(busca)


Ajuda()
