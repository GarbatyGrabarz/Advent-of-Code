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

test_signal = signal[-1]
# This should be in (for line in displayed_digits:) loop
digit = dict()
digit['235'] = set()
digit['069'] = set()
segment = dict()

# Find basic numbers
for encoded_digit in test_signal:
    dl = len(encoded_digit)
    if dl == 2:
        digit[1] = set(encoded_digit)
        dig1478 += 1

    elif dl == 3:
        digit[7] = set(encoded_digit)
        dig1478 += 1

    elif dl == 4:
        digit[4] = set(encoded_digit)
        dig1478 += 1

    elif dl == 7:
        digit[8] = set(encoded_digit)
        dig1478 += 1

segment['up'] = digit[7] - digit[1]

# Find crucial segments
for encoded_digit in test_signal:
    dl = len(encoded_digit)
    if dl == 6:
        s = (digit[8] - set(encoded_digit)) & digit[1]
        if s != 0:
            segment['ur'] = s

# for encoded_digit in test_signal:
#     dl = len(encoded_digit)
#     if dl == 6:
#         s = (digit[8] - set(encoded_digit)) - segment['ul']
#         if s != 0:
#             segment['ur'] = s

# segment['mid'] = digit[4] - digit[1] - segment['ul']
# segment['dr'] = (digit[1] & digit[4] & digit[7]) - segment['ur']
