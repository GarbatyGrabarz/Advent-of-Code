import csv
import statistics

with open('inputs/input7.txt') as f:
    reader = csv.reader(f)
    data = list(reader)

data = [int(x) for x in data[0]]

closest_location = int(statistics.median(data))
fuel_consumption = 0
for loc in data:
    fuel_consumption += abs(loc - closest_location)

print(
    f'The lowest consumption ({fuel_consumption} units) is for '
    f'position {closest_location}')

consumption = list()
for pos in range(max(data)):
    real_fuel_consumption = 0
    for loc in data:
        d = abs(loc - pos)
        real_fuel_consumption += d * (d + 1) / 2
    consumption.append(int(real_fuel_consumption))

fuel_consumption_mkII = min(consumption)
optimal_position = consumption.index(fuel_consumption_mkII)
print(
    f'The lowest real consumption ({fuel_consumption_mkII} units) is for '
    f'position {optimal_position}')
