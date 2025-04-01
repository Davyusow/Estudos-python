#!/usr/bin/env python3
from random import randint
from time import sleep
import emoji

jogador = int(input('Suas escolhas:\n'
'[ 0 ] PEDRA ✊️\n'
'[ 1 ] PAPEL 🖐️\n'
'[ 2 ] TESOURA .✌️\n'
'Qual é a sua jogada? '))
computador = randint(0,2)
jogada = ['Pedra ✊️','Papel 🖐️','Tesour ✌️']    #lista usada no print
if(0 <= jogador <=2):   # se a jogada for válida
    print('JO');sleep(1);print('KEN');sleep(1);print('PO!!') #mostra um texto de cada vez em um espaço de 1 segundo
    #imprime as jogada
    print('Computador jogou {}\n'
    'Jogador jogou {}'.format(jogada[computador],jogada[jogador]))
    #lógica de todas as jogadas
    if(jogador == computador):
        print('EMPATE')
    elif(jogador == 0 and computador == 1 ):
        print('Computador vence')
    elif(jogador == 0 and computador == 2 ):
        print('Jogador vence')
    elif(jogador == 1 and computador == 0 ):
        print('Jogador vence')
    elif(jogador == 1 and computador == 2 ):
        print('Computador vence')
    elif(jogador == 2 and computador == 0 ):
        print('Computador vence')
    elif(jogador == 2 and computador == 1 ):
        print('Jogador vence')
else:
    print('Jogada inválida')
    