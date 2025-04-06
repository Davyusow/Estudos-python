#!/usr/bin/env python3
try:#tenta esse bloco
    a = int(input('Digite o numerador: '))
    b = int(input('Digite o denominador: '))
    r = a / b
except (ValueError,TypeError):#se der problema com o valor ou sendo de outro tipo
    print('{}Tivemos um erro com os tipos de de dados que você digitou!{}'.format('\033[31m','\033[m'))
except ZeroDivisionError:
    print('{}Um número não pode ser divido por 0!{}'.format('\033[31m','\033[m'))
except KeyboardInterrupt:
    print('{}O usuário preferiu não informar os dados!{}'.format('\033[31m','\033[m'))
except Exception as erro:
    print('{}O erro encontrado foi {}{}'.format('\033[31m',erro.__cause__,'\033[m'))
else:#senão, prossiga #opcional
    print(f'O resultado é: {r:.1f}')
finally:#dando certo ou errado, faz isso no final #opcional
    print('Volte sempre!')
