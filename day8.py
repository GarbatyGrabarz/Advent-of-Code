with open('inputs/input8small.txt', 'r') as input_file:
    input_data = input_file.read().splitlines()
input_data = [entry.split(' | ') for entry in input_data]

displayed_digits = [entry[1].split(' ') for entry in input_data]
signal = [entry[0].split(' ') for entry in input_data]
del input_file, input_data

# Arranging each digit aplhabetiaclly
for i in range(len(displayed_digits)):
    for j in range(len(displayed_digits[i])):
        displayed_digits[i][j] = ''.join(sorted(displayed_digits[i][j]))

# Arranging each signal aplhabetiaclly
for i in range(len(signal)):
    for j in range(len(signal[i])):
        signal[i][j] = ''.join(sorted(signal[i][j]))

# Looking for 1, 4, 7 or 8
dig1478 = 0
for line in displayed_digits:
    for encoded_digit in line:
        dl = len(encoded_digit)
        if dl == 2 or dl == 3 or dl == 4 or dl == 7:
            dig1478 += 1

print(f'There are {dig1478} instances of digits 1, 4, 7 or 8')
