#!/usr/bin/env python3

escolha = str(input('Digite o sexo da pessoa [M/F]: ')).upper()
while(escolha != 'M' and escolha != 'F'):
    escolha = str(input('{}Opção inválida!{}, insira o sexo da pessoa: '.format('\033[31m','\033[m'))).upper()
print('Sexo {} registrado com sucesso!'.format(escolha))
