#!/usr/bin/env python3

largura = float(input('Largura da parede em metros: '))
altura = float(input('Altura da parede em metros: '))
area = largura * altura

print('Sua parede tem a dimensão de {}x{}, e sua área é de {}m²'.format(largura,altura,area))
print('Para pintar essa parede você precisará de {}l de tinta'.format(area/2))
