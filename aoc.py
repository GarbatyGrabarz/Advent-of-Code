import pandas

# Loading input
with open(r'input1.txt', 'r') as file:
    input = file.readlines()

sonar_data = pandas.DataFrame(input, columns=['depth'])
sonar_data = sonar_data.astype(int)
del input

# Puzzle 1
sonar_data['delta'] = sonar_data.depth.diff()
depth_increase = sonar_data.delta[sonar_data.delta > 0].count()
