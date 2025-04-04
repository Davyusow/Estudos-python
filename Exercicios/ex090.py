#!/usr/bin/env python3

 #<5 reprovado,5>= & <7 recuperação, >7 aprovado
aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))

if(aluno['Média']<5): aluno['Situação'] = 'Reprovado'
elif(aluno['Média']>=5 and aluno['Média']<7): aluno['Situação'] = 'Recuperação'
else:aluno['Situação'] = 'Aprovado'
print(f'O nome é {aluno["Nome"]}\n' \
f'Sua média é igual à {aluno["Média"]}\n' \
f'Sua situação é {aluno["Situação"]}')
