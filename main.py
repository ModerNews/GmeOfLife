import pygame
from logic import generate_a_new_generation, count_alive_cells, future_table
from pygame.locals import *
import random
import time

def count_alive_cells(table):
    alive_cells_count = 0
    for y in range(0, len(table)):
        for x in range(0, len(table[y])):
            if table[y][x] == 1:
                alive_cells_count += 1
    return alive_cells_count


# Tworzenie planszy
# rows_num = int(input("Jak wiele rzędów? "))
# columns_num = int(input("Jak wiele kolumn? "))
rows_num = 10
columns_num = 10
table = []
future_table = []
for r in range(0, rows_num + 1):
    table.append([])
    future_table.append([])
    for c in range(0, columns_num):
        table[r].append(random.choice([0, 1]))
        future_table[r].append(0)
# Tworzenie nowej generacji
def generate_a_new_generation(table):
    range_x_min = 0
    range_x_max = 0
    range_y_min = 0
    range_y_max = 0
    neighbour_count = 0
    for y in range(0, len(table)):
        for x in range(0, len(table[y])):
            neighbour_count = 0
            range_x_min = x-1
            if range_x_min < 0:
                range_x_min = rows_num - 1
            range_x_max = x + 1
            if range_x_max > rows_num-1:
                range_x_max = 0
            range_y_min = y-1
            if range_y_min < 0:
                range_y_min = columns_num - 1
            range_y_max = y+1
            if range_y_max > columns_num - 1:
                range_y_max = 0
            for vertical in [range_y_min, y, range_y_max]:
                for horizontal in [range_x_min, x, range_x_max]:
                    if table[vertical][horizontal] == 1:
                        neighbour_count += 1
            if table[y][x] == 1:
                #Trzeba odjąć jeden, bo w kodzie powyżej zlicza samego siebie jako sąsiada :/
                neighbour_count -= 1
                if neighbour_count == 2 or neighbour_count == 3:
                    future_table[y][x] = 1
                else:
                    future_table[y][x] = 0
            if table[y][x] == 0:
                if neighbour_count == 3:
                    future_table[y][x] = 1
                else:
                    future_table[y][x] = 0


pygame.init()
width, height = (rows_num) * 45, columns_num * 45
screen = pygame.display.set_mode((width, height))

sprites = []
bit = pygame.image.load("res/bit.png")
buttonStart = pygame.image.load("res/buttonS.png")
buttonPause = pygame.image.load("res/buttonP.png")
sprites.append(bit)
sprites.append(buttonPause)
sprites.append(buttonStart)

i = 0


# for i in range(0, len(table) - 1):
#     print(table[i])
generate_a_new_generation(table)
table = future_table
running = True

pygame.display.set_caption("Game of Life")
pygame.display.set_icon(pygame.image.load("res/Corona0.png"))
while 1:
    while running:
        generate_a_new_generation(table)
        table = future_table

        screen.fill((255, 255, 255))
        lengY = len(table) - 1
        for y in range(lengY):
            lengX = len(table[y])
            for x in range(lengX):
                val = table[y][x]
                if val == 1:
                    screen.blit(bit, ((x + 1) * 45 - 45, (y + 1) * 45))
        time.sleep(0.35)
        screen.blit(buttonStart, (0, 0))
        screen.blit(buttonPause, (45, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if 0 <= pos[0] <= 45 and 0 <= pos[1] <= 45:
                    running = True
                    print(running)
                elif 45 <= pos[0] <= 90 and 0 <= pos[1] <= 45:
                    running = False
                    print(running)

    while not running:
        screen.fill((255, 255, 255))
        lengY = len(table) - 1
        for y in range(lengY):
            lengX = len(table[y])
            for x in range(lengX):
                val = table[y][x]
                if val == 1:
                    screen.blit(bit, ((x + 1) * 45 - 45, (y + 1) * 45))
        time.sleep(0.35)
        screen.blit(buttonStart, (0, 0))
        screen.blit(buttonPause, (45, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if 0 <= pos[0] <= 45 and 0 <= pos[1] <= 45:
                    running = True
                    print(running)
                elif 45 <= pos[0] <= 90 and 0 <= pos[1] <= 45:
                    running = False
                    print(running)
