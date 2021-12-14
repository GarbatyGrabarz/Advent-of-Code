import pandas
import numpy


def frequency_list(rules):
    """ Preparing empty frequency matrix """
    char_pairs = list(rules.keys())
    the_list = pandas.Series(
        data=numpy.zeros(len(char_pairs)),
        index=char_pairs)
    return the_list


def polymerize(freq_list):
    """ Inserting letters """
    global instructions
    available_pairs = freq_list[freq_list > 0]
    freq_list = frequency_list(instructions)  # Clean the frequency list

    for key, val in available_pairs.iteritems():
        for pair in instructions[key]:
            freq_list[instructions[key][pair]] += val

    return freq_list


# ------ Getting data ---------------------------------------------------------
with open('inputs/input14.txt', 'r') as file:
    template = file.readline()
    template = template.replace('\n', '')
    _ = file.readline()
    data = file.read().splitlines()

# ------ Getting instructions and unique letters ------------------------------
instructions = dict()
letters = list()

for line in data:
    segment = line.split(' -> ')[0]
    insert = line.split(' -> ')[1]
    instructions[segment] = insert
    letters.append(insert)

letters = set(letters)

for key in instructions:
    instructions[key] = {
        0: key[0] + instructions[key],
        1: instructions[key] + key[1]}

# ------ Populating frequency matrix ------------------------------------------
freq = frequency_list(instructions)
for i in range(len(template) - 1):
    pair = template[i] + template[i + 1]
    freq[pair] += 1

# ------ Making polymers ------------------------------------------------------
steps = 40
for step in range(steps):
    freq = polymerize(freq)
    if step + 1 in [10, 40]:
        summary = pandas.Series(
            data=numpy.zeros(len(letters)),
            index=letters)

        for ltr in letters:
            s_letter = [x for x in instructions.keys() if x.startswith(ltr)]
            e_letter = [x for x in instructions.keys() if x.endswith(ltr)]
            start = 0
            end = 0
            for pair in s_letter:
                start += freq[pair]

            for pair in e_letter:
                end += freq[pair]

            summary[ltr] = max([start, end])

        diff = int(summary.max() - summary.min())

        print('The difference between most and least abundant element '
              f'after {step + 1} steps is {diff}')
