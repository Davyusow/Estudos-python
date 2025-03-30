#!/usr/bin/env python3

cidade = str(input('Em que cidade você nasceu? '))
cidade = cidade.strip() #remove os espaços em branco
cidade = cidade.lower() #deixa todas as letras minúsculas para facilitar a verificação
print('A cidade começa com santo? ',end='') #end='' faz com que a linha não seja pulada
print('santo' in cidade[:5]) #se 'santo' estiver nos 5 primeiros carácteres da string, retorna verdadeiro