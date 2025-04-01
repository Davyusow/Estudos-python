#!/usr/bin/env python3

cont = 'S'
n1 = int(input('Digite um número inteiro: '))
maior = n1 ; menor = n1
i=1
media = n1

while(cont != 'N'):
    cont = str(input('Deseja inserir outro número?(S/N) ')).strip().upper()
    if(cont != 'S' and cont != 'N'):
        print('{}Opção inválida!{}'.format('\033[31m','\033[m'))
    elif(cont == 'S'):
        n1 = int(input('Digite um número inteiro: '))
        if(menor>n1): menor = n1
        if(maior<n1): maior = n1
        i+=1
        media+=n1
print('A média entre os valores digitados é de {}\n'
'O maior número digitado foi {}\n'
'E o menor foi {}'.format(media/i,maior,menor))
