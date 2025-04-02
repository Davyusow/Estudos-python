#!/usr/bin/env python3

maisque18 = 0
homens = 0
Mmenosque20 = 0

while(True):
    print('\n{} Cadastre uma Pessoa {}'.format('-'*5,'-'*5))
    idade = int(input('Digite o sua idade: '))
    while(True):
        sexo = str(input('Digite o seu sexo:'
        '\n[ M ] : Masculino'
        '\n[ F ] : Feminino\n')).strip().upper()
        if(sexo != 'M' and sexo != 'F'): print('{}Opção inválida, escolha entre M ou F{}'.format('\033[31m','\033[m'))
        else:break
    while(True):
        escolha = str(input('Deseja inserir outra pessoa?[S/N]: ')).strip().upper()
        if(escolha != 'S' and escolha != 'N'): print('{}Opção inválida, escolha entre S ou N{}'.format('\033[31m','\033[m'))
        else: break
    if(idade>18):maisque18+=1
    if(sexo == 'M'):homens+=1
    if(sexo == 'F' and idade<20):Mmenosque20+=1
    if(escolha == 'N'): break
print('\n{}{} Fim do programa {}{}\n'.format('\033[34m','='*5,'='*5,'\033[m'))
print(f'{maisque18} pessoas tem mais de 18 anos\n'
f'{homens} homens foram cadastrados\n'
f'E {Mmenosque20} mulheres tem menos de 20 anos')
