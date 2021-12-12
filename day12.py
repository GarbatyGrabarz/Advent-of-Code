""" Navigate trhough caves """


class underwater(object):

    caves = dict()  # List of all caves
    have_time = True

    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.neighbour = list()
        self.visited = False
        self.visits = 0
        underwater.caves[name] = self

    def add_connection(address):
        if address[0] not in underwater.caves:
            if address[0].islower():
                size = 'small'
            else:
                size = 'large'
            underwater(address[0], size)
        underwater.caves[address[0]].neighbour.append(address[1])

    def sort_addresses():
        for cave in underwater.caves:
            underwater.caves[cave].neighbour.sort()

    def reset_visits():
        for cave in underwater.caves:
            underwater.caves[cave].visits = 0


def find_all_paths(current, destination, path=list()):
    global all_paths
    current = underwater.caves[current]

    if current.size == 'small':  # For normal graphs all visited are marked
        current.visited = True

    elif current.size == 'large':
        current.visited = False

    path.append(current.name)

    if current.name != destination:
        for i in current.neighbour:
            if underwater.caves[i].visited is False:  # All non visited
                find_all_paths(i, destination)  # Repeat
    else:
        # print(path)
        all_paths.append(path.copy())

    path.pop()  # Remove last non-end element so you can keep exploring
    current.visited = False
    return path


def find_all_paths_time(current, destination, path=list()):

    def special_case(pth):
        small = [x for x in pth if x.islower() and x not in ['start', 'end']]
        # print(small)
        if len(small) == len(set(small)):
            return True
        else:
            return False

    global all_paths2
    current = underwater.caves[current]

    if current.size == 'small':
        current.visited = True

    elif current.size == 'large':
        current.visited = False

    path.append(current.name)

    if current.name != destination:
        for i in current.neighbour:

            if underwater.caves[i].visited is False:
                find_all_paths_time(i, destination)

            # Added exception for one 2 visits to a small cave
            elif (
                    underwater.caves[i].visited
                    and special_case(path)
                    and underwater.caves[i].name not in ['start', 'end']):

                find_all_paths_time(i, destination)

    else:
        # print(path)
        all_paths2.append(path.copy())

    path.pop()
    if current.size == 'small':
        current.visited = current.name in path
    elif current.size == 'large':
        current.visited = False
    return path


# ------ Loading data ------------------------------------
with open('inputs/input12.txt', 'r') as file:
    input_file = list(file.read().splitlines())

data = [x.split('-') for x in input_file]

# ------ Adding all connections --------------------------
for line in data:
    underwater.add_connection(line)
    line.reverse()
    underwater.add_connection(line)
underwater.sort_addresses()

# ------ Looking for valid paths -------------------------
all_paths = list()
find_all_paths('start', 'end')
print(f'There are {len(all_paths)} valid paths through the cave system')

# ------ Looking for valid paths but have some time ------
all_paths2 = list()
find_all_paths_time('start', 'end')
print(f'With more time we have {len(all_paths2)} valid paths')
