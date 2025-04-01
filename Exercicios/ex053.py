#!/usr/bin/env python3

frase = str(input('Digite uma frase: ')).strip().lower()
frase = frase.replace(' ','')   #remove o espaço do texto
com = frase[::-1]   #inverte o texto
resposta = 1
for i in range(0,len(frase)):
    if(com [i] != frase[i]):
        resposta = -1
        break
if(resposta ==1):
    print('A frase é um palindromo!')
else:
    print('A frase não é um palindromo!')
