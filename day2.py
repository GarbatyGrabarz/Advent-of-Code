import pandas


class submarine(object):

    def __init__(self):
        self.horizonal = 0
        self.depth = 0

    def execute(self, command, value):
        if command == 'forward':
            self.go_forward(value)
        elif command == 'up':
            self.go_up(value)
        elif command == 'down':
            self.go_down(value)
        else:
            print('Something went wrong')

    def go_forward(self, value):
        self.horizonal += value

    def go_down(self, value):
        self.depth += value

    def go_up(self, value):
        self.depth -= value

    def position_status(self):
        h = self.horizonal
        d = self.depth
        print(f'I am {h} units away at the depth of {d} units.')

    def depth_and_horizontal(self):
        return self.horizonal * self.depth

    def read(self, instructions):
        instructions.value = instructions.value.astype(int)
        for index, row in instructions.iterrows():
            c = row['command']
            v = row['value']
            self.execute(c, v)


class submarine_mkII(submarine):

    def __init__(self):
        super().__init__()
        self.aim = 0

    def go_down(self, value):
        self.aim += value

    def go_up(self, value):
        self.aim -= value

    def go_forward(self, value):
        self.horizonal += value
        self.depth += value * self.aim


instructions = pandas.read_csv(
    r'inputs/input2.txt',
    names=['command', 'value'],
    delimiter=' ')

elven_submarine = submarine()
elven_submarine.read(instructions)
elven_submarine.position_status()
depthhorizon = elven_submarine.depth_and_horizontal()
print(f'Depth times position factor is {depthhorizon}\n')

print('IMPROVED CONTROLS')
improved_elven_submarine = submarine_mkII()
improved_elven_submarine.read(instructions)
improved_elven_submarine.position_status()
depthhorizon = improved_elven_submarine.depth_and_horizontal()
print(f'Depth times position factor is {depthhorizon}')
