from math import gcd


def generate_maze(maze_data):
    graph = {}
    for line in maze_data:
        current_node = line[:3]
        left_node, right_node = line[7:-2].split(', ')
        graph[current_node] = {}
        graph[current_node]['L'] = left_node
        graph[current_node]['R'] = right_node
    return graph


def navigate_maze(maze, current_node, steps):
    current_step = 0
    while not current_node.endswith('Z'):
        current_node = maze[current_node][steps[current_step % len(steps)]]
        current_step = current_step + 1
    return current_step


def lcm(nums):
    lcm = 1
    for i in nums:
        lcm = (lcm * i) // gcd(lcm, i)
    return lcm


def navigate_simultaneous_maze(maze, steps):
    # get starting nodes
    starting_nodes = [i for i in maze if i.endswith('A')]

    # instead of computing all of the paths and stepping through, we can
    # determine the length of the path each starting node initiates.
    # the number of steps required to complete all paths is then the
    # lcm of these lengths
    cycle_lengths = []

    # get the cycle length for each starting node
    for node in starting_nodes:
        cycle_lengths.append(navigate_maze(maze, node, steps))

    # return the lcm
    return lcm(cycle_lengths)



if __name__ == "__main__":
    with open("input.txt") as data:
        steps = data.readline().strip()
        data.readline() # skip empty line between header and body
        maze = generate_maze(data)
        print(navigate_simultaneous_maze(maze, steps))
