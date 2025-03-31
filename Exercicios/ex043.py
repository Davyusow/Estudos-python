#!/usr/bin/env python3

peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (pow(altura,2))
print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if(imc < 18.5):
    print('IMC abaixo do peso')
elif(imc >= 18.5 and imc < 25):
    print('IMC com peso ideal')
elif(imc >= 25 and imc < 30):
    print('IMC com sobrepeso')
elif(imc >= 30 and imc < 40):
    print('IMC com obesidade')
elif(imc >=40):
    print('IMC com obesidade mórbida')
