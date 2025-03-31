#!/usr/bin/env python3

nome = str(input('Digite seu nome: '))
if(nome == 'Gustavo'):
    print('Que nome bonito!')
elif(nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo'):    #elif é a mesma coisa que o else if (senão se)
    print('Seu nome é bem popular no Brasil!')
elif(nome in 'Ana Cláudia Jéssica Juliana'):
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal.')

print('Tenha um bom dia {}!'.format(nome))
