import pandas

# Loading input
with open(r'inputs/input3.txt', 'r') as file:
    input = file.readlines()

inn = [list(x.replace('\n', '')) for x in input]
diagnostic_report = pandas.DataFrame(inn)
diagnostic_report = diagnostic_report.astype(int)

bitsummary = diagnostic_report[diagnostic_report > 0].count()
allbits = len(diagnostic_report)

gamma_rate = list()
epsilon_rate = list()

for bit in bitsummary:
    if bit > allbits / 2:
        gamma_rate.append('1')
        epsilon_rate.append('0')
    else:
        gamma_rate.append('0')
        epsilon_rate.append('1')

gamma_rate = ''.join(gamma_rate)
epsilon_rate = ''.join(epsilon_rate)

gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)
print(f'Gamma rate: {gamma_rate}')
print(f'Epsilon rate: {epsilon_rate}')

power_consumption = gamma_rate * epsilon_rate
print(f'The power consumption is: {power_consumption}')
