#!/usr/bin/env python3

print('{} FEIRINHA DAVUSOW {}'.format('='*10,'='*10))
compra = float(input('Preço da compra: R$'))
escolha = int(input('FORMAS DE PAGAMENTO\n'
'[ 1 ] à vista dinheiro/cheque\n'
'[ 2 ] à vista cartão\n'
'[ 3 ] 2x no cartão\n'
'[ 4 ] 3x ou mais no cartão\n'
'Qual opção? '))

if(escolha == 1):
    print('Sua compra de R${:.2f} irá valer R${:.2f} no final'.format(compra,compra*0.9))
elif(escolha == 2):
    print('Sua compra de R${:.2f} irá valer R${:.2f} no final'.format(compra,compra*0.95))
elif(escolha == 3):
    print('Sua compra de R${:.2f} irá valer R${:.2f} no final'.format(compra,compra))
elif(escolha == 4):
    print('Sua compra de R${:.2f} irá valer R${:.2f} no final'.format(compra,compra*1.2))
else:
    print('Opção inválida!\033]31m\n')