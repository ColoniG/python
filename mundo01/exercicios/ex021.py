import pygame
pygame.init()
pygame.mixer.music.load("C:/Users/colon/OneDrive/Área de Trabalho/Cursos/python/mundo01/exercicios/extra/tlou.mp3")
pygame.mixer.music.play()
input()
pygame.event.wait()

print("Acabou de tocar")

