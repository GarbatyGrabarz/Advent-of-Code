""" Playing bingo with a squid - checking winning bingo boards"""

import pandas
import numpy
from itertools import count


class bingo_module(object):

    def __init__(self, df):
        self.board = df
        self.ssum = numpy.nan
        self.winnum = numpy.nan

    def check(self, number):
        """ Replace found number with NaN """
        i, c = numpy.where(self.board == number)
        if len(i) != 0 and len(c) != 0:
            self.board.iloc[i[0], c[0]] = numpy.nan
            # print(f'Lucky number: {number}')

    def winner(self):
        """ Counts not-NaN in rows and colums.
        If one is empty it is a winner """
        columns = self.board.count().to_list()
        rows = self.board.transpose().count().to_list()
        if 0 in columns or 0 in rows:
            return True
        else:
            return False

    def get_sum(self):
        self.ssum = self.board.sum().sum()

    def play_bingo(self, numbers):
        draw_number = count(1)
        for number in numbers:
            draw = next(draw_number)
            self.check(number)
            if self.winner():
                self.get_sum()
                self.winnum = number
                self.draw = draw
                break


with open('Inputs/input4num', 'r') as input_file:
    lucky_numbers = input_file.readlines()
lucky_numbers = lucky_numbers[0].split(',')
lucky_numbers = [int(x) for x in lucky_numbers]

# Load boards
with open('Inputs/input4brd', 'r') as input_file:
    bingo_lines = input_file.readlines()
bingo_lines = [ln.replace('\n', '') for ln in bingo_lines if ln != '\n']

brdnum = count(1)
boards = dict()
for i in range(0, len(bingo_lines), 5):
    matrix = list()
    for j in range(5):
        num_line = bingo_lines[i + j].split(' ')
        num_line = [int(x) for x in num_line if x != '']
        matrix.append(num_line)
    board_number = next(brdnum)
    matrix = pandas.DataFrame(data=matrix)
    boards[f'b{board_number}'] = matrix

results = pandas.DataFrame()

for bid in boards:
    print(f'\r{bid} / 100   ', end='\r')
    b = bingo_module(boards[bid])
    b.play_bingo(lucky_numbers)
    r = {
        'index': bid,
        'ssum': b.ssum,
        'drawn': b.draw,
        'winning': b.winnum}
    results = results.append(r, ignore_index=True)
results = results.set_index('index')

# Determining the best board
winning_board = results[results.drawn == results.drawn.min()]
wboard = winning_board.index[0]
wdraw = int(winning_board.drawn[0])
wsum = int(winning_board.ssum[0])
wnumber = int(winning_board.winning[0])
wscore = wsum * wnumber

print(f'The first board to win is {wboard}. It takes {wdraw} draws to win '
      f'with the sum of remaining numbers equal to '
      f'{wsum}. The lucky number is {wnumber}')
print(f'The final score is {wscore:.0f}\n')

# Determining the worst board
losing_board = results[results.drawn == results.drawn.max()]
lboard = losing_board.index[0]
ldraw = int(losing_board.drawn[0])
lsum = int(losing_board.ssum[0])
lnumber = int(losing_board.winning[0])
lscore = lsum * lnumber

print(f'The last board to win is {lboard}. It takes {ldraw} draws to win '
      f'with the sum of remaining numbers equal to '
      f'{lsum}. The lucky number is {lnumber}')
print(f'The final score is {lscore:.0f}\n')
