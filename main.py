import pygame
from settings import *

pygame.init()

pygame.font.init()

(width, height) = (WIDTH, HEIGHT)

window = pygame.display.set_mode((width, height))

pygame.display.set_caption('Todo-py-qt')

pygame.display.flip()

is_running = True

font = pygame.font.SysFont("comicsansms", 15)


rect = pygame.Surface((720, 480))
pygame.draw.rect(rect, RED, (0, 0, 720, 480), 1)

todo = ['git init', 'make breakfast']
doing = ['add pic']
done = ['update facebook']


text = font.render(todo[0], True, RED)


def draw_grid(window, scale, color):
    for x in range(0, WIDTH, int(TILESIZE * scale)):
        pygame.draw.line(window, color, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, int(TILESIZE * scale)):
        pygame.draw.line(window, color, (0, y), (WIDTH, y))


def draw_rect(window, x, y, width, height, color):
    pygame.draw.line(window, color, (x, y), (x + width, y))
    pygame.draw.line(window, color, (x, y), (x, y + height))
    pygame.draw.line(window, color, (x, y + height), (x + height, y + height))
    pygame.draw.line(window, color, (x + width, y), (x + height, y + height))


while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False
        print(pygame.mouse.get_pos())
    # draw_grid(window, 1, DARKGRAY)
    # window.blit(rect,(30,30))
    # pygame.draw.rect(window, RED, (30,30, 720,480))
    draw_rect(window, 30, 45, 600, 600, RED)
    draw_rect(window, 660, 45, 600, 600, BLUE)
    window.blit(text, (48,63))

    pygame.display.flip()
    pygame.display.update()

pygame.quit()
