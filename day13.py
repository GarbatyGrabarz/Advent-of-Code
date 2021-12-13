import numpy
from matplotlib import pyplot


with open('inputs/input13.txt', 'r') as file:
    dot_map = file.read().splitlines()
break_line = dot_map.index('')
instructions = dot_map[break_line + 1:]
dot_map = dot_map[:break_line]

# Fill the paper with dots
dot_map = numpy.genfromtxt(dot_map, delimiter=',').astype(int)
Xsize = dot_map[:, 0].max() + 1
Ysize = dot_map[:, 1].max() + 1
paper = numpy.zeros((Ysize, Xsize)).astype(int)

for x, y in dot_map:
    paper[y, x] += 1

plot_paper = True

if plot_paper:
    fig, _ = pyplot.subplots(1)
    pyplot.axis('off')
    fig.axes[0].imshow(paper)
    fig.axes[0].patch.set_alpha(0.01)
    del fig

instructions = [x.replace('fold along ', '').split('=') for x in instructions]


def fold(matrix, steps, plot_folds):
    axis = steps[0]
    fold = int(steps[1])

    if axis == 'y':
        for row in range(fold, matrix.shape[0]):
            matrix[2*fold - row, :] += matrix[row, :]
        matrix = matrix[:fold, :]

    elif axis == 'x':
        for column in range(fold, matrix.shape[1]):
            matrix[:, 2*fold - column] += matrix[:, column]
        matrix = matrix[:, :fold]

    matrix[matrix > 1] = 1

    if plot_folds:
        fig, _ = pyplot.subplots(1)
        pyplot.axis('off')
        fig.axes[0].imshow(matrix)
        fig.axes[0].patch.set_alpha(0.01)
        del fig

    return matrix


plot_folds = False
for num, instruction in enumerate(instructions):
    paper = fold(paper, instruction, plot_folds)
    if num == 0:
        dots = numpy.count_nonzero(paper > 0)
        print(f'There are {dots} visible dots after first fold')

if plot_paper and not plot_folds:
    fig, _ = pyplot.subplots(1)
    pyplot.axis('off')
    fig.axes[0].imshow(paper)
    fig.axes[0].patch.set_alpha(0.01)
    del fig
