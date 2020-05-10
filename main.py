import pygame
from settings import *

pygame.init()

pygame.font.init()

(width, height) = (WIDTH, HEIGHT)

window = pygame.display.set_mode((width, height))

pygame.display.set_caption('Todo-py-qt')

pygame.display.flip()

is_running = True

# font = pygame.font.SysFont("comicsansms", 15)
font = pygame.font.Font('res/JetBrainsMono-Regular.ttf', 15)


rect = pygame.Surface((720, 480))
pygame.draw.rect(rect, RED, (0, 0, 720, 480), 1)

todo = ['git init', 'make breakfast']
doing = ['add pic']
done = ['update facebook']


text = []

print(len(todo))
for i in range(0, len(todo)):
    text[i] = font.render(todo[i], True, RED)
    print(i)
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


x = 30
y = 45

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False
            if event.key == pygame.K_DOWN or event.key == pygame.K_j:
                y += 30
            if event.key == pygame.K_UP or event.key == pygame.K_k:
                y -= 30
            if event.key == pygame.K_RIGHT or event.key == pygame.K_l:
                x = 660
                y = 45
            if event.key == pygame.K_LEFT or event.key == pygame.K_h:
                x = 30
                y = 45
        print(pygame.mouse.get_pos())
    window.fill(BLACK)
    draw_grid(window, 1, DARKGRAY)
    # window.blit(rect,(30,30))
    # pygame.draw.rect(window, RED, (30,30, 720,480))
    draw_rect(window, 30, 45, 600, 600, YELLOW)
    draw_rect(window, 660, 45, 600, 600, YELLOW)
    pygame.draw.rect(window, YELLOW2, (x, y, 600, 30))
    # window.blit(text, (45, 50))
    # window.blit(text, (45, 50 + 30))
    for t in text:
        window.blit(t, (45, 50 + j))
        j += 30

    pygame.display.flip()
    pygame.display.update()

pygame.quit()
