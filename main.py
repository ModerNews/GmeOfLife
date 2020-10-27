import pygame
from logic import generate_a_new_generation, count_alive_cells, future_table
from pygame.locals import *

pygame.init()
width, height = 1000, 1000
screen = pygame.display.set_mode((width, height))

player = pygame.image.load("res/bit.png")
i = 0
table = []


for i in range(0, len(table) - 1):
    print(table[i]);

while 1:
    i += 10
    screen.fill(0)
    for y in range(len(table) - 1):
        for x in range(len(table[y]) - 1):
            screen.blit(player, (x, y))
    pygame.display.flip()
    print("Done")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
