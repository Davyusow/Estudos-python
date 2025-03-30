#!/usr/bin/env python3

#Fatiamento
frase = 'Curso em Vídeo Python'
print(frase[9:14]) #9 é o primeiro valor e 14 é o valor limite que não será impresso
print(frase[9:21])
print(frase[9:21:2]) #9 e 21 são o espaço que será considerado, o :2 é o passo, ou seja
#imprime a cada 2 carácters
print(frase[:5])    #omite o início, portanto
#todos os caractéres antes do quinto índice serão impressos
print(frase[15:]) #omite o fim, portanto
#todos os caractéres apartir do 15° índice serão impressos
print(frase[9::3])
#a cada 3 carácteres apartir do nono indíce serão impressos 

#Análise
print(len(frase)) #imprime o tamanho da frase
print(frase.count('o')) #conta quantas vezes aparece o carácter 'o'
print(frase.count('o',0,13)) #conta quantas vezes aparece o carácter 'o' apartir 0 até o 13° indíce
print(frase.find('deo')) #retorna o indice que 'deo' começa
print(frase.find('Android')) #caso não encontre, retorna -1
print('Curso' in frase) #retorna um valor booleano se 'Curso' existe na string frase

#transformação
print(frase.replace('Python','Android'))    #troca 'Python' por 'Android'
print(frase.upper())    #faz todas as letras ficarem maiúsculas
print(frase.lower())    #faz todas as letras ficarem minúsculas
print(frase.capitalize())
print(frase.title())
frase = '   Aprenda Python  '
print(frase)
print(frase.strip())    #remove os espaços no início e no fim da string
print(frase.rstrip())   #remove os espaços no fim da string
print(frase.lstrip())   #remove os espaços no início da string

#Divisão
frase = 'Curso em Vídeo Python'
lista = frase.split() #separa a palavras uma em cada string
print('-'.join(lista))  #junta um array de Strings com '-' como separador
