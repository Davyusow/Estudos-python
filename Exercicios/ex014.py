#!/usr/bin/env python3

n1 = float(input('Informe a temperatura em °C: '))
conv = n1 * 9/5 + 32
print('A temperatura de {:.1f}°C corresponde à {:.1f}°F!'.format(n1,conv))