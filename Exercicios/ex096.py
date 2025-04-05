#!/usr/bin/env python3
def area(base,altura):
    resultado = base*altura
    print(f'A área de um terreno {base}x{altura} é de {resultado}m²')


print(f'Controle de Terrenos\n{"-"*30}')
largura = float(input('Largura (m): '))
altura = float(input('Comprimento (m): '))
area(largura,altura)

