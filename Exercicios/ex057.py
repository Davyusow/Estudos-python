#!/usr/bin/env python3

cont = 1
while(cont < 11):
    escolha = str(input('Digite o sexo da {}° pessoa [M/F]: '.format(cont))).upper()
    if(escolha == 'M' or escolha == 'F'):
        cont+=1
    else:
        print('{}Opção inválida!, Tente Novamente!{}'.format('\033[31m','\033[m'))
