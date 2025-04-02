#!/usr/bin/env python3

top20 = ('Fotaleza','Juventude','Vasco','Cruzeiro','Grêmio','Red Bull Bragatino','Ceará',
'Corinthians','Flamengo','Internacional','Bahia','São Paulo','Sport','Botafogo','Palmeiras',
'Atlético-MG','Santos','Mirassol','Fluminense','Vitória')   #2 de abril de 2025

print('{} Top 5 {}'.format('-'*5,'-'*5))
for i in range(0,5):
    print(f'{i+1}° - {top20[i]}')

print('{} Últimos 4 {}'.format('-'*5,'-'*5))
for i in range(19,15,-1):
    print(f'{i+1}° - {top20[i]}')

Ordenado = sorted(top20)

print('{} Ordem Alfabética {}'.format('-'*5,'-'*5))
for i in range(0,20):
    print(f'{i+1:2}° - {Ordenado[i]}')
print('-'*25)

print(f'O time Red Bull Bragatino está na {top20.index("Red Bull Bragatino")+1}° posição do placar')
