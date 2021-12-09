""" Running diagnostics - analysis of a signel bit-by-bit"""

import pandas

# Loading input
with open(r'inputs/input3', 'r') as file:
    input = file.readlines()

""" Loading each bit to a separate column of a dataframe is a bit crazy.
Perhaps a regular loops would be suficient """
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
print(f'The power consumption is: {power_consumption}\n')

# Part 2
o2 = diagnostic_report.copy()
co2 = diagnostic_report.copy()


def find_bit_value(report, bit_type):
    """ This feels like an overcomplicated solution.
    Since I opperate on logical values there must be a beter way.
    I should come back to this after some years
    and imprement something more elegant """
    for col in report.columns:
        allbits = len(report)
        if allbits == 1:
            break
        ones = report[col][report[col] == 1].count()
        zeros = report[col][report[col] == 0].count()

        if bit_type == 'most':
            if ones >= zeros:
                bt = 1
            else:
                bt = 0
        elif bit_type == 'least':
            if ones >= zeros:
                bt = 0
            else:
                bt = 1

        report = report[report[col] == bt]

    binary = ''.join([str(x) for x in report.iloc[0].to_list()])
    rate = int(binary, 2)
    return rate


o2_gen_rate = find_bit_value(o2, 'most')
print(f'Oxygen generator rating: {o2_gen_rate}')

co2_scrubb_rate = find_bit_value(co2, 'least')
print(f'CO2 scrubber rating: {co2_scrubb_rate}')

life_support = o2_gen_rate * co2_scrubb_rate
print(f'Life support rating: {life_support}')
