import modulos
import json  
import os  

if os.path.exists("Exercicios/ex115/cadastrados.json"):
    with open("Exercicios/ex115/cadastrados.json", "r") as arquivo:
        Lista = json.load(arquivo)
else:
    Lista = []  # Se o arquivo não existe, inicia uma lista vazia

while(True):
    modulos.Titulo('MENU PRiNCIPAL: ')
    print('1 - Ver Pessoas Cadastradas: ')
    print('2 - Cadastrar nova Pessoa: ')
    print('3 - Sair do programa')
    try:
        opcao = int(input('Sua opção: '))
    except ValueError:
        print('{}Digite um valor inteiro!{}'.format('\033[31m','\033[m'))
    else:
        if(opcao < 1 or opcao >3):print('{}Inira um valor entre 1 e 3!{}'.format('\033[31m','\033[m'))
        elif(opcao == 1):
            modulos.Listar(Lista)
        elif(opcao == 2):
            temp = modulos.Cadastrar()
            Lista.append(temp)
            with open("Exercicios/ex115/cadastrados.json", "w") as arquivo:
                json.dump(Lista, arquivo, indent=4)
        elif(opcao == 3):
            print('Opção 3')
            break
print('Obrigado, volte sempre!')

