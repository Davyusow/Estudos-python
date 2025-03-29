#!/usr/bin/env python3
import pygame   #pode ser meio chatinho mas precisa instalar essa biblioteca aqui

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('Exercicios/ex021.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy(): #enquanto o audio estiver tocando
    pygame.time.Clock().tick(10)    #o timer esṕera o audio terminar 
