#!/usr/bin/env python3

#open("caminho","r")

#MODOS:
# r - leitura
# a - Incrementa
# w - escrita
# x - criar arquivo
# r+ - Leitura + escrita

arquivo = open("Teste01/ManipulaçãoDeArquivos/teste","a") # abre o arquivo para inserção
#print(arquivo.readable()) #verifica se o arquivo pode ser lido
#print(arquivo.read()) #imprime o arquivo na tela, pode ser jogado em uma variável
#print(arquivo.readline())#Lê a primeira linha do arquivo, para ler a próxima é necessário chamar a função novamente
#Lista = arquivo.readlines() #retorna as linhas em forma de índice, facilitando para a manipulação de litas
#print(Lista)

arquivo.write("\nC++") #insere um texto no arquivo pulando uma linha

arquivo.close() #fecha o arquivo, senão ele fica aberto em segundo plano mesmo após o fecamento do programa
