#!/usr/bin/env python3

n1 = float(input('Quanto dinheiro você tem na carteira?: R$'))
print('Com R${:.2f}, você pode comprar ${:.2f} doláres. '.format(n1,n1/5.76)) #cotação do dólar às 00:45 de 29 de março de 2025
print('€{:.2f} euros. '.format(n1/6.23)) #cotação do euro às 00:45 de 29 de março de 2025
print('¥{:.2f} ienes. '.format(n1/0.038)) #cotação do iene às 00:45 de 29 de março de 2025
