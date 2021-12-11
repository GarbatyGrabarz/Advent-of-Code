""" Dumbo Octopus - lighting up your neighbours """

import numpy

with open('inputs/input11.txt', 'r') as file:
    data = list(file.read().splitlines())

data = [list(line) for line in data]
data = numpy.array(data).astype(float)
data2 = data.copy()

flashes = 0
steps = 100
Max_Y, Max_X = data.shape

neighbours = {
    (-1, 1),
    (-1, 0),
    (-1, -1),
    (0, -1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1)}


def infect(data):
    global flashes
    flashed = False
    for y, row in enumerate(data):  # Scan rows
        for x, value in enumerate(row):  # Scan columns
            if data[y, x] > 9:
                flashes += 1
                data[y, x] = numpy.nan
                flashed = True
                for dy, dx in neighbours:  # Check all neghbours
                    if 0 <= y + dy < Max_Y and 0 <= x + dx < Max_X:
                        data[y + dy, x + dx] += 1
                infect(data)
    return flashed


for step in range(1, steps + 1):
    data += 1
    infect(data)
    reset = numpy.isnan(data)
    data[reset] = 0

print(f'{flashes} flashes have been observed')

step = 1
while True:
    data2 += 1
    infect(data2)
    reset = numpy.isnan(data2)
    data2[reset] = 0
    occurrences = numpy.count_nonzero(data2 == 0)
    if occurrences == Max_Y * Max_X:
        print(f'All octopuses will light up on step {step}')
        break
    step += 1
