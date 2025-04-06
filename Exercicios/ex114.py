#!/usr/bin/env python3
import urllib
import urllib.request

try:
    urllib.request.urlopen("https://www.pudim.com.br")
except:
    print('{}O site não está acessível no momento!{}'.format('\033[31m','\033[m'))
else:
    print('Consegui acessar o site!')


