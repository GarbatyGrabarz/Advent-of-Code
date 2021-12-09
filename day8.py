""" Investigating scrabled 7-segment screen signal """

with open('inputs/input8.txt', 'r') as input_file:
    input_data = input_file.read().splitlines()
input_data = [entry.split(' | ') for entry in input_data]

displayed_digits = [entry[1].split(' ') for entry in input_data]
signal = [entry[0].split(' ') for entry in input_data]
del input_file, input_data

# Arranging each digit alphabetically and turn them to sets
for i in range(len(displayed_digits)):
    for j in range(len(displayed_digits[i])):
        displayed_digits[i][j] = set(''.join(sorted(displayed_digits[i][j])))

# Arranging each signal alphabetically and turn them to sets
for i in range(len(signal)):
    for j in range(len(signal[i])):
        signal[i][j] = set(''.join(sorted(signal[i][j])))

# Looking for 1, 4, 7 or 8
dig1478 = 0
for line in displayed_digits:
    for encoded_digit in line:
        dl = len(encoded_digit)
        if dl == 2 or dl == 3 or dl == 4 or dl == 7:
            dig1478 += 1
print(f'There are {dig1478} instances of digits 1, 4, 7 or 8')

digit = dict()
segment = dict()
sum_of_outputs = 0

for i in range(len(signal)):
    for encoded_digit in signal[i]:
        dl = len(encoded_digit)
        if dl == 2:
            digit[1] = encoded_digit
            dig1478 += 1

        elif dl == 3:
            digit[7] = encoded_digit
            dig1478 += 1

        elif dl == 4:
            digit[4] = encoded_digit
            dig1478 += 1

        elif dl == 7:
            digit[8] = encoded_digit
            dig1478 += 1

    for encoded_digit in signal[i]:
        dl = len(encoded_digit)
        if dl == 6:
            s = (digit[8] - encoded_digit) & digit[1]
            if len(s) == 1:
                segment['NW'] = s

        elif dl == 5:
            s = ((digit[8] - encoded_digit) - digit[1]) & digit[4]
            if len(s) == 1:
                segment['NE'] = s

    segment['N'] = digit[7] - digit[1]
    segment['SW'] = (digit[7] & digit[4] & digit[1]) - segment['NW']
    segment['mid'] = digit[4] - digit[1] - segment['NE']

    for encoded_digit in signal[i]:
        dl = len(encoded_digit)
        if dl == 5:
            s = (
                digit[8]
                - encoded_digit
                - segment['NW']
                - segment['SW']
                - segment['NE'])
            if len(s) == 1:
                segment['SE'] = s

    segment['S'] = digit[8] - digit[4] - segment['N'] - segment['SE']
    segment['H_lines'] = segment['N'] | segment['mid'] | segment['S']

    digit[0] = digit[8] - segment['mid']
    digit[2] = segment['H_lines'] | segment['NW'] | segment['SE']
    digit[3] = segment['H_lines'] | segment['NW'] | segment['SW']
    digit[5] = segment['H_lines'] | segment['NE'] | segment['SW']
    digit[6] = digit[8] - segment['NW']
    digit[9] = digit[8] - segment['SE']

    display = 0
    multiplayer = 1000
    for dig in displayed_digits[i]:
        for key in digit:
            if digit[key] == dig:
                display += (key * multiplayer)
                multiplayer /= 10

    sum_of_outputs += int(display)

print(f'The sum of all outputs is {sum_of_outputs}')
