#!/usr/bin/env python3

n1 = float(input('Digite uma medida em metros: '))
print('A medida {:.1f}m corresponde à:'.format(n1))
print('{:.3f}km'.format(n1/1000))
print('{:.2f}hm'.format(n1/100))
print('{:.1f}dam'.format(n1/10))
print('{}dm'.format((n1*10)))
print('{}cm'.format((n1*100)))
print('{}mm'.format((n1*1000)))
