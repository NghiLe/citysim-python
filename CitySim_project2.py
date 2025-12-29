import numpy as np
import os
import time
import random

ESC = '\x1b'
RESET = ESC + '[0m'

GRASS = ESC + '[42m' + ESC + '[30m' + '.' + RESET
HOUSE = ESC + '[47m' + ESC + '[30m' + '#' + RESET
STREET = ESC + '[40m' + ESC + '[33m' + '=' + RESET
RIVER = ESC + '[44m' + ESC + '[97m' + '~' + RESET
DEMOLISH = ESC + '[41m' + ESC + '[97m' + 'x' + RESET
EARTHQUAKE = ESC + '[43m' + ESC + '[33m' + 'z' + RESET
VOLCANO = ESC + '[48;5;124m' + ESC + '[38;5;196m' + 'v' + RESET

population = 0
rev = 0

size = int(input("Enter city size: "))
city_map = np.full((size, size), GRASS, dtype=object)

def print_city(city):
    os.system("clear")
    for i in range(size):
        for j in range(size):
            print(city[i, j], end="")
        print()
    print(f"Population: {population}")
    print(f"Revenue: ${rev}")

def demolish(y, x):
    global population, rev
    cell = city_map[y, x]
    if cell in [HOUSE, STREET, RIVER]:
        city_map[y, x] = DEMOLISH
        if cell == HOUSE:
            population -= 1
            rev -= 200
        elif cell == STREET:
            rev -= 50
        elif cell == RIVER:
            rev -= 50

def build_house(y, x):
    global population, rev
    for a in [0,1]:
        for b in [0,1]:
            ny, nx = y + a, x + b
            if ny < size and nx < size:
                if city_map[ny, nx] not in [GRASS, DEMOLISH]:
                    city_map[ny, nx] = DEMOLISH
                else:
                    city_map[ny, nx] = HOUSE
                    population += 1
                    rev += 200

def build_street(y, x):
    global rev
    for i in range(4):
        nx = x + i
        if nx < size:
            if city_map[y, nx] not in [GRASS, DEMOLISH]:
                city_map[y, nx] = DEMOLISH
                rev -= 50
            else:
                city_map[y, nx] = STREET
                rev += 50

def build_river(y, x):
    global rev
    for i in range(3):
        ny = y + i
        if ny < size:
            if city_map[ny, x] not in [GRASS, DEMOLISH]:
                city_map[ny, x] = DEMOLISH
                rev -= 50
            else:
                city_map[ny, x] = RIVER
                rev += 50

def earthquake():
    print("EARTHQUAKE! The ground is shaking!")
    time.sleep(0.5)
    for blink in range(5):
        temp = np.full((size, size), EARTHQUAKE, dtype=object)
        print_city(temp)
        time.sleep(0.25)
        print_city(city_map)
        time.sleep(0.25)
    total_cells = size * size
    num_affected = total_cells // 3
    all_coords = [(i,j) for i in range(size) for j in range(size)]
    affected = random.sample(all_coords, num_affected)
    for (y, x) in affected:
        if city_map[y, x] in [HOUSE, STREET, RIVER]:
            demolish(y, x)
    print("Earthquake ended, some buildings were destroyed!")
    time.sleep(1)
    print_city(city_map)

def volcano():
    print("VOLCANO ERUPTION! Lava is flowing down the city!")
    time.sleep(0.5)
    temp_map = city_map.copy()
    for y in range(size):
        for x in range(size):
            if temp_map[y, x] != RIVER:
                temp_map[y, x] = VOLCANO
        print_city(temp_map)
        time.sleep(0.2)
    total_cells = size * size
    num_destroyed = total_cells * 35 // 100
    all_coords = [(i,j) for i in range(size) for j in range(size)]
    random.shuffle(all_coords)
    destroyed = all_coords[:num_destroyed]
    for (y, x) in destroyed:
        if city_map[y, x] in [HOUSE, STREET, RIVER]:
            demolish(y, x)
    print("The eruption ended! The city is safe again.")
    time.sleep(1)
    print_city(city_map)

# Main loop
turn = 0
while True:
    print_city(city_map)
    try:
        y,x = [int(i) for i in input("Pick coordinate to build HOUSE: ").split()]
        if 0 <= y < size and 0 <= x < size:
            build_house(y, x)
        else:
            print("Out of range")
            continue
        print_city(city_map)

        y,x = [int(i) for i in input("Pick coordinate to build STREET: ").split()]
        if 0 <= y < size and 0 <= x < size:
            build_street(y, x)
        else:
            print("Out of range")
            continue
        print_city(city_map)

        y,x = [int(i) for i in input("Pick coordinate to build RIVER: ").split()]
        if 0 <= y < size and 0 <= x < size:
            build_river(y, x)
        else:
            print("Out of range")
            continue
        print_city(city_map)

        turn += 1
        if turn % 3 == 0:
            earthquake()
        if turn % 5 == 0:
            volcano()

    except:
        print("Invalid input, try again.")
        continue

