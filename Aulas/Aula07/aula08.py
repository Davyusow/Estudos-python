#!/usr/bin/env python3

nome = input("Qual o seu nome?\n")
print("Prazer em te conhecer {:20}!".format(nome))  # Nome escrito em 20 espaços
print(
    "Prazer em te conhecer {:>20}!".format(nome)
)  # nome alinhado a direita em 20 espaços
print(
    "Prazer em te conhecer {:<20}!".format(nome)
)  # nome alinhado a esquerda em 20 espaços
print(
    "Prazer em te conhecer {:^20}!".format(nome)
)  # nome alinhado no meio em 20 espaços
print(
    "Prazer em te conhecer {:=^20}!".format(nome)
)  # nome alinhado no meio em 20 espaços com '=' em volta
print(f"")  # NOVA FORMA DAVYUSON!!!!!!!!!
