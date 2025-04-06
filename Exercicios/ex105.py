#!/usr/bin/env python3
def Notas(*nota,situacao=False):
    """
    →Retorna um dicionário com as informações de uma sala
    incluindo quantidade,maior nota,menor nota,média e opcionalmente a situação da sala
    :param *nota: Uma lista de notas de 0 a 10.0
    :param situacao: Define se a situação da sala será ou não inclusa
    :return : retorna um dicionário com todas as informações
    """
    media = 0
    if(len(nota)>0):maior = nota[0] ;menor = nota[0]
    else:maior = 0 ;menor = 0
    for i in range(0,len(nota)):
        media+=nota[i]
        if(nota[i]>maior):maior = nota[i]
        if(nota[i]<menor):menor = nota[i]
    media/=len(nota)
    if (situacao==True):
        if(media>=7):resposta = 'BOA'
        elif(media >= 5 and media < 7): resposta = 'RAZOÁVEL'
        elif(media < 5): resposta = 'RUIM'
        return {'Quantidade':len(nota),'Maior':maior,'Menor':menor,'Média':media,'Situação':resposta}    
    return {'Quantidade':len(nota),'Maior':maior,'Menor':menor,'Média':media}


resp = Notas(5.5, 9.5, 10, 6.5)
print(resp)
