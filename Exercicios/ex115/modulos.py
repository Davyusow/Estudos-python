#!/usr/bin/env python3


def Titulo(txt):
    print(f'{"-"*30}\n{txt:^30}\n{"-"*30}')

def Cadastrar():
    Titulo('CADASTRO')
    nome = str(input('Digite seu nome: '))
    while(True):
        valido = False
        try:
            idade = int(input(f'Digite sua idade: '))
        except:
            print('{}Digite uma idade válida com um número inteiro!{}'.format('\033[31m','\033[m'))
        else:
            if str(idade).isnumeric(): valido = True; break
    return {'Nome':nome,'Idade':idade}

def Listar(Pessoas):
    Titulo('PESSOAS CADASTRADAS')
    if not Pessoas:
        print("Nenhuma pessoa cadastrada!")
    else:
        for pessoa in Pessoas:  # `pessoa` é cada dicionário na lista
            print(f'Nome: {pessoa["Nome"]:<20}Idade: {pessoa["Idade"]} anos')
