import random;
import pygame;

def count_alive_cells(table):
    alive_cells_count = 0;
    for y in range(0, len(table)):
        for x in range(0, len(table[y])):
            if table[y][x] == 1:
                alive_cells_count += 1;
    return alive_cells_count;
# Tworzenie planszy
rows_num = 10
columns_num = 10
table = [];
future_table = [];
for r in range(0, rows_num + 1):
    table.append([]);
    future_table.append([]);
    for c in range(0, columns_num):
        table[r].append(random.choice([0, 1]));
        future_table[r].append(0);
# Tworzenie nowej generacji
def generate_a_new_generation(table):
    range_x_min = 0;
    range_x_max = 0;
    range_y_min = 0;
    range_y_max = 0;
    neighbour_count = 0;
    for y in range(0, len(table)):
        for x in range(0, len(table[y])):
            neighbour_count = 0;
            range_x_min = x-1;
            if range_x_min < 0:
                range_x_min = rows_num - 1;
            range_x_max = x + 1;
            if range_x_max > rows_num-1:
                range_x_max = 0;
            range_y_min = y-1;
            if range_y_min < 0:
                range_y_min = columns_num - 1;
            range_y_max = y+1;
            if range_y_max > columns_num - 1:
                range_y_max = 0;
            for vertical in [range_y_min,y,range_y_max]:
                for horizontal in [range_x_min,x,range_x_max]:
                    if table[vertical][horizontal] == 1:
                        neighbour_count += 1;
            if table[y][x] == 1:
                #Trzeba odjąć jeden, bo w kodzie powyżej zlicza samego siebie jako sąsiada :/
                neighbour_count -= 1;
                if neighbour_count == 2 or neighbour_count == 3:
                    future_table[y][x] = 1;
                else:
                    future_table[y][x] = 0;
            if table[y][x] == 0:
                if neighbour_count == 3:
                    future_table[y][x] = 1;
                else:
                    future_table[y][x] = 0;


#Pętla, w której po naciśnięciu entera tworzy się nowa generacja
# while count_alive_cells(table) > 0:
#     for i in range(0, len(table) - 1):
#         print(table[i]);
#     generate_a_new_generation(table);
#     table = future_table;
#     print();
#     input();
