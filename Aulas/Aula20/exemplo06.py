#!/usr/bin/env python3
def soma(*valores):
    s = 0
    for i in valores:
        s+=valores
    print(s)

soma(3,5,3,15,2)