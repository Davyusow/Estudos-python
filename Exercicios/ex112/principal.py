#!/usr/bin/env python3
from ex112 import moeda
from ex112.dado import dados

p = dados.leiaDinheiro('Insira um valor monetário: R$')
moeda.resumo(p,80,20) #meio que isso é o 110 e o 109 ao mesmo tempo

