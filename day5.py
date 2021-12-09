""" Avoid vents - finding the spots with most cross-setions """

import pandas

with open('inputs/input5.txt', 'r') as file:
    vents = file.readlines()


def process(text_line):
    text_line = text_line.replace(' -> ', ',')
    text_line = text_line.replace('\n', '')
    text_line = text_line.split(',')
    text_line = [int(x) for x in text_line]
    return text_line


vents = [process(line) for line in vents]
vents = pandas.DataFrame(vents, columns=['x1', 'y1', 'x2', 'y2'])
vent_map = pandas.DataFrame([[0] * 1000] * 1000)
vent_map_mkII = pandas.DataFrame([[0] * 1000] * 1000)


def process_line(data_slice, vmap, diagonals=False):
    if data_slice.x1 == data_slice.x2:
        X = data_slice.x1

        if data_slice.y1 > data_slice.y2:
            r1 = data_slice.y2
            r2 = data_slice.y1
        else:
            r1 = data_slice.y1
            r2 = data_slice.y2

        for Y in range(r1, r2 + 1):
            vmap.iloc[Y, X] += 1

    elif data_slice.y1 == data_slice.y2:
        Y = data_slice.y1

        if data_slice.x1 > data_slice.x2:
            r1 = data_slice.x2
            r2 = data_slice.x1
        else:
            r1 = data_slice.x1
            r2 = data_slice.x2

        for X in range(r1, r2 + 1):
            vmap.iloc[Y, X] += 1

    else:
        if diagonals:
            projection = abs(data_slice.x1 - data_slice.x2)
            if data_slice.x1 > data_slice.x2:
                px = -1
            else:
                px = 1

            if data_slice.y1 > data_slice.y2:
                py = -1
            else:
                py = 1

            X = data_slice.x1
            Y = data_slice.y1
            for Z in range(projection + 1):
                vmap.iloc[Y + Z * py, X + Z * px] += 1

        else:
            pass

    return vmap


data_slices = len(vents)
for index in range(data_slices):
    vent_map = process_line(
        vents.loc[index],
        vent_map)

    vent_map_mkII = process_line(
        vents.loc[index],
        vent_map_mkII,
        diagonals=True)

    progress = index / data_slices
    print(f'\rBuilding vent maps: {progress * 100:.0f}%   ', end='\r')


danger_points = 0
for column in vent_map:
    dangerous_vents = vent_map[column][vent_map[column] >= 2]
    danger_points += len(dangerous_vents)

real_danger_points = 0
for column in vent_map:
    real_dangerous_vents = vent_map_mkII[column][vent_map_mkII[column] >= 2]
    real_danger_points += len(real_dangerous_vents)

print(f'\nThe number of dangerous points is {danger_points}')
print(f'The number of really dangerous points is {real_danger_points}')
