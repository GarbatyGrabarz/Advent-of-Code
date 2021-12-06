import csv


def count_fish(data, days):
    fish = dict()
    new_fish = dict()
    for number in range(9):
        fish[number] = len([x for x in data if x == number])

    for day in range(days):
        for n in range(8):
            new_fish[n] = fish[n + 1]
            if n == 6:
                new_fish[n] += fish[0]
        new_fish[8] = fish[0]
        fish = new_fish
        new_fish = dict()
        print(f'\rDay {day} of {days}  ', end='\r')

    fish_no = 0
    for num in range(9):
        fish_no += fish[num]

    print(f'The number of fish after {days} days is {fish_no}')


with open('inputs/input6.txt', newline='\n') as f:
    reader = csv.reader(f)
    data = list(reader)

input_fishes = [int(x) for x in data[0]]

count_fish(input_fishes, 80)
count_fish(input_fishes, 256)
