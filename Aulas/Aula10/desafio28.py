#!/usr/bin/env python3
import random

num1 = random.randint(0,5)

num2 = int(input('Chute um número de 0 a 5'))
if(num2==num1):
    print('Acertou')
else:
    print('Errou')