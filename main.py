import pygame
from settings import *

pygame.init()

pygame.font.init()

(width, height) = (WIDTH, HEIGHT)

window = pygame.display.set_mode((width, height))

pygame.display.set_caption('Todo-py-qt')

is_running = True

# font = pygame.font.SysFont("comicsansms", 15)
font = pygame.font.Font('res/JetBrainsMono-Regular.ttf', 15)

rect = pygame.Surface((720, 480))
pygame.draw.rect(rect, RED, (0, 0, 720, 480), 1)

# global variables
todo_render = [] # list of task to render
sel_x = 30 # select x position
sel_y = 60 # select y position

# TODO: get the data from json
todo = ['git init', 'make breakfast']
doing = ['add pic']
done = ['update facebook']


for i in range(0, len(todo)):
    todo_render.append(font.render(todo[i], True, RED))
    

def draw_grid(window, scale, color):
    for x in range(0, WIDTH, int(TILESIZE * scale)):
        pygame.draw.line(window, color, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, int(TILESIZE * scale)):
        pygame.draw.line(window, color, (0, y), (WIDTH, y))


def draw_rect(window, x, y, width, height, color):
    pygame.draw.line(window, color, (x, y), (x + width, y))
    pygame.draw.line(window, color, (x, y), (x, y + height))
    pygame.draw.line(window, color, (x, y + height), (x + width, y + height))
    pygame.draw.line(window, color, (x + width, y), (x + width, y + height))


while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False
            if event.key == pygame.K_DOWN or event.key == pygame.K_j:
                sel_y += 30
            if event.key == pygame.K_UP or event.key == pygame.K_k:
                sel_y -= 30
            if event.key == pygame.K_RIGHT or event.key == pygame.K_l:
                sel_x = 660
                sel_y = 45
            if event.key == pygame.K_LEFT or event.key == pygame.K_h:
                sel_x = 30
                sel_y = 45
        print(pygame.mouse.get_pos())
    window.fill(BLACK)
    draw_grid(window, 1, DARKGRAY) # draw background grids for easy measurement
    draw_rect(window, 30, 60, 600, 600, YELLOW)  # right rectangle container
    draw_rect(window, 660, 60, 600, 600, YELLOW)  # left rectangle container
    draw_rect(window,0,675,1279, 30, RED) # command rectangle
    pygame.draw.rect(window, YELLOW2, (sel_x, sel_y, 600, 30))  # select rectangle
    

    j = 0
    for t in range(0, len(todo_render)):
        window.blit(todo_render[t], (45, 65 + j))
        j += 30

    pygame.display.flip()
    pygame.display.update()


pygame.quit()
