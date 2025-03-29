#!/usr/bin/env python3
from math import hypot

n1 = float(input('Comprimento do cateto oposto: '))
n2 = float(input('Comprimento di cateto adjascente: '))
hipotenusa = (n1**2) + (n2**2)
#hipotenusa = math.hypot(n1,n2) #math.hypot() faz todo o cálculo da hipotenusa
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa**(1/2)))

