import os
from random import random

import readchar

POS_X = 0
POS_Y = 1

MAP_WIDTH = 20
MAP_HEIGHT = 15

NUM_OF_MAPS_OBJETCS = 11

my_position = [3, 1]
tail_lenght = 0
map_objects = []

# Generate random objects on the maps
while len(map_objects) < NUM_OF_MAPS_OBJETCS:
    new_position = ([random.randint(0, MAP_WIDTH), random.randint(0, MAP_HEIGHT)])


    if new_position not in map_objects and new_position != my_position:
        map_objects.append(new_position)


# main loop
while True:

    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = " "
            object_in_cell = None

            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = "*"
                    object_in_cell = map_object


            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = "@"

                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_lenght += 1

            print(" {} ".format(char_to_draw), end="")
        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")

    # Donde te quieres mover

    # direction = input("¿Donde te quieres mover? [WASD]: ")

    direction = readchar.readchar().decode()

    if direction == "W":
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "S":
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "A":
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "D":
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == 'q':
        break

    os.system("cls")


