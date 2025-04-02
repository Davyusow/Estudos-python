#!/usr/bin/env python3

maisQueMil=0

print('{} Lojão do Batatão {}'.format('-'*5,'-'*5))
nome = str(input('Nome do produto: '))
preco = float(input('Preço: R$'))

if(preco>1000):maisQueMil+=1
menorP = preco
total = preco    

while(True):
    escolha = str(input('Deseja adicionar outro? [S/N] ')).strip().upper()
    if(escolha != 'S' and escolha != 'N'): print('{}Opção inválida!{}'.format('\033[31m','\033[m'))
    elif(escolha == 'S'):
        nome = str(input('Nome do produto: '))
        preco = float(input('Preço: R$'))
        total+=preco
        if(preco>1000):maisQueMil+=1
        if(preco<menorP): 
            menorP = preco
            menorN = nome
    elif(escolha == 'N'):break

print(f'O total gasto foi R${total:.2f}\n'
f'{maisQueMil} produtos custam mais que R$1000\n'
f'E o produto mais barato foi {menorN}, que custa {menorP}')
