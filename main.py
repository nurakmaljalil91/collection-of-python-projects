import pygame

(width , height) = (300, 300)

window = pygame.display.set_mode((width, height))

pygame.display.set_caption('Todo-py-qt')

pygame.display.flip()

is_running = True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False