#!/usr/bin/env python3

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2)/2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1,n2,media))

if(media < 5):
    print('O aluno está REPROVADO')
elif(media >= 5 and media < 7):
    print('O aluno está em RECUPERAÇÃO')
elif(media > 7):
    print('O aluno está APROVADO')