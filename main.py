import pygame
import json
import pygame_textinput
from settings import *

pygame.init()

pygame.font.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Todo-py-qt')

is_running = True

# font = pygame.font.SysFont("comicsansms", 15)
font = pygame.font.Font('res/JetBrainsMono-Regular.ttf', 15)

# global variables
todo_render = []  # list of task to render
date_render = []  # lisd of the task date
sel_x = 30  # select x position
sel_y = 60  # select y position
todo_color = YELLOW
header = 'PS D:/Onedrive/Dev/todo-py>py main.py'
act_input = False
cn_add_tsk = False # allow to add task
del_cn_add_tsk = False # allow to add task
is_prs_inp = False
read_task = ''
# Create TextInput-object
textinput = pygame_textinput.TextInput('','res/JetBrainsMono-Regular.ttf',15, True, YELLOW, YELLOW)
taskinput = pygame_textinput.TextInput('','res/JetBrainsMono-Regular.ttf',15, True, BLUE, BLUE)


header_render = font.render(header, True, YELLOW)

# TODO: get the data from json
with open('data.json') as f:
    data = json.load(f)



def add_task(new_task):
    temp = {"id": 4,"item": new_task, "date":"13/05/2020"}
    print(temp)
    

# draw background grid
def draw_grid(window, scale, color):
    for x in range(0, WIDTH, int(TILESIZE * scale)):
        pygame.draw.line(window, color, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, int(TILESIZE * scale)):
        pygame.draw.line(window, color, (0, y), (WIDTH, y))


# draw rectangle
def draw_rect(window, x, y, width, height, color):
    pygame.draw.line(window, color, (x, y), (x + width, y))
    pygame.draw.line(window, color, (x, y), (x, y + height))
    pygame.draw.line(window, color, (x, y + height), (x + width, y + height))
    pygame.draw.line(window, color, (x + width, y), (x + width, y + height))


# pygame.key.set_repeat(60, 60)  # allow keyboard repeat press (delay,interval)
# app loop
while is_running:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN or event.key == pygame.K_j:
                if not act_input:
                    sel_y += 30
            if event.key == pygame.K_UP or event.key == pygame.K_k:
                if not act_input:
                    sel_y -= 30
            if event.key == pygame.K_RIGHT or event.key == pygame.K_l:
                if not act_input:
                    sel_x = 660
                    sel_y = 60
            if event.key == pygame.K_LEFT or event.key == pygame.K_h:
                if not act_input:
                    sel_x = 30
                    sel_y = 60
            if event.key == pygame.K_1:
                act_input = True
            if event.key == pygame.K_2:
                act_input = False
                # print('escape')
            # print(pygame.mouse.get_pos())
    if act_input:
        if textinput.update(events):
            print(textinput.get_text())
            prs_inp = textinput.get_text()
            textinput.clear_text()
            is_prs_inp = True 
            if cn_add_tsk:
                read_task = textinput.get_text()
        if cn_add_tsk:
            if taskinput.update(events):
                add_task(taskinput.get_text())
                cn_add_tsk = False
                taskinput.clear_text()
            # if textinput.get_text() == ':quit!':
            #     is_running = False
            # if textinput.get_text() == ':q':
            #     is_running = False
            # if textinput.get_text() == ':addTask':
            #     pygame.time.delay(1)
            #     cn_add_tsk = True
            #     textinput.clear_text()
            # if del_cn_add_tsk:
            #     add_task(textinput.get_text())
            #     textinput.clear_text()
            # else:
            #     textinput.clear_text()
           
    # print(textinput.update(events))

    # delay logic
    # if cn_add_tsk:
    #     del_cn_add_tsk = True
    # if del_cn_add_tsk is False:
    #     cn_add_tsk = True
    
    # other method of read input
    if is_prs_inp:
        if prs_inp == ':q':
            is_running = False
        if prs_inp == ':addTask':
            cn_add_tsk = True
            is_prs_inp = False
            prs_inp = ''
        
    # update here
    # print(del_cn_add_tsk)
    for d in data:
        todo_render.append(font.render(d['task'], True, todo_color))
        date_render.append(font.render(d['date'], True, todo_color))

    # print(read_tasks)
    # render here
    # print(act_input)  
    window.fill(BLACK)  # reset background color
    # draw background grids for easy measurement
    draw_grid(window, 1, DARKGRAY)
    window.blit(header_render, (0, 3))
    draw_rect(window, 30, 60, 600, 600, YELLOW)  # right rectangle container
    draw_rect(window, 660, 60, 600, 600, YELLOW)  # left rectangle container
    draw_rect(window, 0, 675, 1279, 30, YELLOW)  # input command rectangle
    pygame.draw.rect(window, YELLOW2, (sel_x, sel_y, 600, 30))  # select rect
    
    # window.blit(txt_inp_ren, (3, 678))
    # Blit its surface onto the screen
    window.blit(textinput.get_surface(), (3, 678))
    if cn_add_tsk:
        window.blit(taskinput.get_surface(), (3, 678))
    next_line = 0
    for t in range(0, len(todo_render)):
        window.blit(todo_render[t], (45, 65 + next_line))
        window.blit(date_render[t], (500, 65 + next_line))
        next_line += 30
    
    todo_render.clear()
    date_render.clear()
    # if txt_inp == ':addTask!':
    #     txt_inp = ':'
    pygame.display.flip()
    pygame.display.update()


pygame.quit()
