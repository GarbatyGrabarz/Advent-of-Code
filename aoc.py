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

# Puzzle 2
window = 3
indexer = pandas.api.indexers.FixedForwardWindowIndexer(window_size=window)
sonar_data['window_sum'] = sonar_data.depth.rolling(window=indexer).sum()

sonar_data['delta_w'] = sonar_data.window_sum.diff()
depth_inc_improved = sonar_data.delta_w[sonar_data.delta_w > 0].count()
