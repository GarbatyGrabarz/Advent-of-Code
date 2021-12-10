""" Navigation syntax error and autocompletion"""

with open('inputs/input10.txt', 'r') as file:
    input_data = file.read().splitlines()

opposite = {
      '(': ')',
      '[': ']',
      '{': '}',
      '<': '>'}

score_error = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137}

score_autocorrect = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4}

line_counter = 0
corrupted = list()
syntax_error_score = 0

# ------ Finding corrupted lines ---------------------------------------
for line in input_data:
    line = list(line)

    # Clean valid chunks
    while True:
        for i in range(len(line) - 1):
            if line[i + 1] == opposite.get(line[i]):
                line[i+1] = '.'
                line[i] = '.'
        mod = len([x for x in line if x == '.'])
        line = [x for x in line if x != '.']
        if mod == 0:
            break

    for ch in line:
        if ch in {')', ']', '}', '>'}:
            syntax_error_score += score_error.get(ch)
            corrupted.append(line_counter)
            break
    line_counter += 1

print(f'Syntax error score for the corrupted lines is {syntax_error_score}')

# ------ Fixing incompleted lines ---------------------------------------
corrupted = [input_data[x] for x in corrupted]
for corr in corrupted:
    input_data.remove(corr)

autocorrect_scores = list()

for line in input_data:
    line = list(line)

    # Clean valid chunks
    while True:
        for i in range(len(line) - 1):
            if line[i + 1] == opposite.get(line[i]):
                line[i+1] = '.'
                line[i] = '.'
        mod = len([x for x in line if x == '.'])
        line = [x for x in line if x != '.']
        if mod == 0:
            break

    line.reverse()
    autocorrect = [opposite.get(x) for x in line]
    score = 0
    for ch in autocorrect:
        score *= 5
        score += score_autocorrect.get(ch)

    autocorrect_scores.append(score)
autocorrect_scores.sort()
winning_score = autocorrect_scores[int(len(autocorrect_scores) / 2)]

print(f'Autocompletion winning score is {winning_score}')
