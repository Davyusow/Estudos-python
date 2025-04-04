#!/usr/bin/env python3

Aluno = ['Nome','nota1','nota2']
Lista = []

Aluno[0] = str(input('Nome: '))
Aluno[1] = int(input('Nota1: '))
Aluno[2] = int(input('Nota2: '))
Lista.append(Aluno[:])
Aluno.clear()

while(True):
    prox = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if(prox != 'N' and prox != 'S'): print('{}Opção inválida!{}'.format('\033[31m','\033[m'))
    elif(prox == 'N'): break
    elif(prox == 'S'):
        Aluno.append(str(input('Nome: ')))
        Aluno.append(float(input('Nota1: '))) 
        Aluno.append(float(input('Nota2: ')))
        Lista.append(Aluno[:])
        Aluno.clear()

print('No.    Nome               Média')
for i in range(0, len(Lista)):
    print(f'{i}      {Lista[i][0]:20} {(Lista[i][1]+Lista[i][2])/2:<13}')
#Análise dos Dados
while(True):
    procura = int(input('Mostrar as notas de qual aluno?[999] interrompe: '))
    if(procura > -1 and procura < len(Lista)):
        print(f'As notas de {Lista[procura][0]} são {Lista[procura][1:]}')
    elif(procura == 999):
        break
    else:
        print('{}Aluno não encontrado!{}'.format('\033[31m','\033[m'))
print('Finalizando')
