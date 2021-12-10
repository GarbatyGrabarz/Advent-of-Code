""" Smoke map - finding local minima in 2D map """

import numpy
from matplotlib import pyplot
import scipy

with open('inputs/input9.txt', 'r') as file:
    input_data = file.read().splitlines()

data = list()
for row in input_data:
    line = [int(x) for x in list(row)]
    data.append(list(line))
data = numpy.array(data)

max_x = data.shape[1]
max_y = data.shape[0]
minima = list()
point_counter = 0

for x in range(max_x):
    for y in range(max_y):

        neighbour = dict()
        if x - 1 >= 0:
            if data[y, x] < data[y, x - 1]:
                neighbour['W'] = True
            else:
                neighbour['W'] = False

        if x + 1 <= max_x - 1:
            if data[y, x] < data[y, x + 1]:
                neighbour['E'] = True
            else:
                neighbour['E'] = False

        if y - 1 >= 0:
            if data[y, x] < data[y - 1, x]:
                neighbour['N'] = True
            else:
                neighbour['N'] = False

        if y + 1 <= max_y - 1:
            if data[y, x] < data[y + 1, x]:
                neighbour['S'] = True
            else:
                neighbour['S'] = False

        local_min = True
        for key in neighbour:
            local_min *= neighbour[key]
        if local_min:
            minima.append((y, x))

        point_counter += 1
        print(f'\rChecked points: {point_counter}/{data.size}  ', end='\r')

risk_level = 0
for point in minima:
    risk_level += 1 + data[point[0], point[1]]

print(f'The risk level of the smoke is {risk_level}')

fig, _ = pyplot.subplots(1)
pyplot.axis('off')
fig.axes[0].imshow(data)
fig.axes[0].patch.set_alpha(0.01)
fig.savefig(
    'Images/Smoke map.png',
    dpi=600,
    bbox_inches='tight',
    transparent=True)


basin_map = data < 9  # Making a mask of elements smaller than 9
labels, labels_number = scipy.ndimage.label(basin_map)
sizes = scipy.ndimage.sum(basin_map, labels, range(labels_number + 1))
sizes.sort()
Three_largest_basins = int(sizes[-3] * sizes[-2] * sizes[-1])

fig2, _ = pyplot.subplots(1)
pyplot.axis('off')
fig2.axes[0].imshow(labels)
fig2.axes[0].patch.set_alpha(0.01)
fig2.savefig(
    'Images/Basin map.png',
    dpi=600,
    bbox_inches='tight',
    transparent=True)

print(f'The size of three largest basins multipled is {Three_largest_basins}')
