import pygame
from pygame.locals import *
from random import randint

pygame.init()

def aleatorio_grid():
    x = randint(0, 590)
    y = randint(0, 590)
    x = x//10*10
    y = y//10*10
    return (x, y)

def colisao(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


def game_over(tela):
    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
        font = pygame.font.SysFont("comicsans", 50)
        text = font.render("Game over!", 1, (0, 200, 50))
        tela.fill((255, 255, 255))
        tela.blit(text, (100, 300))
        pygame.display.update()

CIMA = 0
DIREITA = 1
BAIXO = 2
ESQUERDA = 3

cobra = [(200, 200), (210, 200), (220, 200)]
corpo_cobra = pygame.Surface((10, 10))
corpo_cobra.fill((255, 255, 255))

fruta = pygame.Surface((10, 10))
fruta.fill((255, 0, 0))
pos_fruta = aleatorio_grid()

clock = pygame.time.Clock()

direcao = ESQUERDA

velocidade = 10

tela = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Jogo da cobra")

while True:
    clock.tick(velocidade)
    
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()

        if e.type == KEYDOWN:
            if e.key == K_UP:
                direcao = CIMA
            if e.key == K_DOWN:
                direcao = BAIXO
            if e.key == K_RIGHT:
                direcao = DIREITA
            if e.key == K_LEFT:
                direcao = ESQUERDA

    if colisao(cobra[0], pos_fruta):
        pos_fruta = aleatorio_grid()
        for i in range(0, len(cobra)):
            cobra.append((0, 0))
        velocidade += 5

    for i in range(1, len(cobra)):
        if colisao(cobra[0], cobra[i]):
            game_over(tela)
            break
            
    if cobra[0][0] <= 0 or cobra[0][0] >= 600:
        game_over(tela)
        break

    if cobra[0][1] <= 0 or cobra[0][1] >= 600:
        game_over(tela)
        break

    for i in range(len(cobra)-1, 0, -1):
        cobra[i] = (cobra[i-1][0], cobra[i-1][1])

    if direcao == CIMA:
        cobra[0] = (cobra[0][0], cobra[0][1]-10)
    if direcao == BAIXO:
        cobra[0] = (cobra[0][0], cobra[0][1]+10)
    if direcao == DIREITA:
        cobra[0] = (cobra[0][0]+10, cobra[0][1])
    if direcao == ESQUERDA:
        cobra[0] = (cobra[0][0]-10, cobra[0][1])

    
    tela.fill((0, 0, 0))
    tela.blit(fruta, pos_fruta)
    for p in cobra:
        tela.blit(corpo_cobra, p)

    pygame.display.update()