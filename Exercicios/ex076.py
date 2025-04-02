#!/usr/bin/env python3

produtos = ('Lápis',1.75,'Borracha',2.00,'Caderno',15.90,'Estojo',25.00,'Transferidor',4.20,'Compasso',9.99,'Mochila',120.32,'Canetas',22.30,'Livro',34.90)

print('{}\n {:^50} \n{}'.format('-'*50,'Lista de Produtos','-'*50))
for i in range(0,len(produtos),2):
    nome = produtos[i]
    preco = produtos[i + 1]
    print(f"{nome:.<40} R$ {preco:>7.2f}")
print('-'*50)
