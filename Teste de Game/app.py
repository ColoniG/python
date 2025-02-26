import pygame                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    pygame.display.flip()


'''
import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Obtém o tamanho da tela do usuário
info_objeto = pygame.display.Info()
tamanho_janela = (info_objeto.current_w, info_objeto.current_h)

# Configura a janela para o tamanho da tela do usuário
janela = pygame.display.set_mode(tamanho_janela, pygame.FULLSCREEN)

# Configura o personagem
posicao_pacman = [50, 50]
tamanho_pacman = [25, 25]
cor_pacman = (255, 255, 0)  # RGB para amarelo

# Configura a velocidade de movimento
velocidade = 1

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Detecta a entrada do teclado
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        posicao_pacman[0] -= velocidade
    if teclas[pygame.K_RIGHT]:
        posicao_pacman[0] += velocidade
    if teclas[pygame.K_UP]:
        posicao_pacman[1] -= velocidade
    if teclas[pygame.K_DOWN]:
        posicao_pacman[1] += velocidade

    # Desenha o fundo
    janela.fill((0, 0, 0))  # preenche a janela com preto

    # Desenha o Pac-Man
    pygame.draw.rect(janela, cor_pacman, pygame.Rect(posicao_pacman[0], posicao_pacman[1], tamanho_pacman[0], tamanho_pacman[1]))

    # Atualiza a janela
    pygame.display.flip()


#

import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configura o tamanho da janela
tamanho_janela = (800, 600)
janela = pygame.display.set_mode(tamanho_janela)

# Configura o personagem
posicao_pacman = [50, 50]
tamanho_pacman = [50, 50]
cor_pacman = (255, 255, 0)  # RGB para amarelo

# Configura a velocidade de movimento
velocidade = 5

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Detecta a entrada do teclado
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        posicao_pacman[0] -= velocidade
    if teclas[pygame.K_RIGHT]:
        posicao_pacman[0] += velocidade
    if teclas[pygame.K_UP]:
        posicao_pacman[1] -= velocidade
    if teclas[pygame.K_DOWN]:
        posicao_pacman[1] += velocidade

    # Desenha o fundo
    janela.fill((0, 0, 0))  # preenche a janela com preto

    # Desenha o Pac-Man
    pygame.draw.rect(janela, cor_pacman, pygame.Rect(posicao_pacman[0], posicao_pacman[1], tamanho_pacman[0], tamanho_pacman[1]))

    # Atualiza a janela
    pygame.display.flip()

import pygame

# Inicializar o Pygame
pygame.init()

# Configurar a tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pac-Man")

# Carregar imagens do Pac-Man e dos pontos
player_image = pygame.image.load("imagens\pacman.png")
dot_image = pygame.image.load("imagens\dot.png")

# Posições iniciais do jogador e dos pontos
player_x = 300
player_y = 300
dot_x = 100
dot_y = 100

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualizar a lógica do jogo aqui

    # Desenhar elementos na tela
    screen.fill((0, 0, 0))  # Preencher a tela com preto
    screen.blit(player_image, (player_x, player_y))
    screen.blit(dot_image, (dot_x, dot_y))

    # Atualizar a tela
    pygame.display.flip()

# Encerrar o Pygame
pygame.quit()
    
'''