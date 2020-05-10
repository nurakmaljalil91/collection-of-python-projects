import pygame
from settings import *

(width , height) = (WIDTH, HEIGHT)

window = pygame.display.set_mode((width, height))

pygame.display.set_caption('Todo-py-qt')

pygame.display.flip()

is_running = True


rect = pygame.Surface((720,480))
pygame.draw.rect(rect, RED, rect.get_rect, 1)


def draw_grid(window, scale, color):
    for x in range(0, WIDTH, int(TILESIZE * scale)):
        pygame.draw.line(window, color, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, int(TILESIZE * scale)):
        pygame.draw.line(window, color, (0, y), (WIDTH, y))


while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False
        print(pygame.mouse.get_pos())
    draw_grid(window,1, DARKGRAY)
    window.blit(rect, 30,30)
    #pygame.draw.rect(window, RED, (30,30, 720,480))
    pygame.display.flip()
    pygame.display.update()

pygame.quit() 

