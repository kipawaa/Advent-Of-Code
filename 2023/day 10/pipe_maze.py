def get_maze(maze_data):
    graph = {(x,y): [] for x in range(len(maze_data[0])) for y in range(len(maze_data))}
    for y in range(len(maze_data)):
        for x in range(len(maze_data[y])):
            match maze_data[y][x]:
                case '|':
                    if y > 0:
                        graph[(x,y)].append((x,y-1))
                    if y < len(maze_data) - 1:
                        graph[(x,y)].append((x,y+1))
                case '-':
                    if x > 0:
                        graph[(x,y)].append((x-1,y))
                    if x < len(maze_data[y]) - 1:
                        graph[(x,y)].append((x+1,y))
                case 'L':
                    if y > 0:
                        graph[(x,y)].append((x,y-1))
                    if x < len(maze_data[y]) - 1:
                        graph[(x,y)].append((x+1,y))
                case 'J':
                    if y > 0:
                        graph[(x,y)].append((x,y-1))
                    if x > 0:
                        graph[(x,y)].append((x-1,y))
                case '7':
                    if x > 0:
                        graph[(x,y)].append((x-1,y))
                    if y < len(maze_data) - 1:
                        graph[(x,y)].append((x,y+1))
                case 'F':
                    if x < len(maze_data[y]) - 1:
                        graph[(x,y)].append((x+1,y))
                    if y < len(maze_data) - 1:
                        graph[(x,y)].append((x,y+1))
                case 'S':
                    if x > 0:
                        graph[(x,y)].append((x-1,y))
                    if x < len(maze_data[y]) - 1:
                        graph[(x,y)].append((x+1, y))
                    if y > 0:
                        graph[(x,y)].append((x, y-1))
                    if y < len(maze_data) - 1:
                        graph[(x,y)].append((x, y+1))
                case _:
                    pass
    return graph
            
def get_maximum_distance(start, maze, current, depth):
    # if we've re-reached the start then that was a loop!
    print(current)
    if current == start and depth != 0:
        return depth
    
    # find our neighbours
    neighbours = maze[current]
    
    # if we have no neighbours then this isn't a loop
    if neighbours == []:
        return 0

    # make sure we don't get re-visited
    maze[current] = []
    
    # find the longest loop following any of our neighbours
    return max(get_maximum_distance(start, maze, neighbour, depth+1) for neighbour in neighbours)

#def get_maximum_distance(maze_data):
#    # read rather than readlines so that we can find start easily
#    maze_data = maze_data.read()
#    start = maze_data.index('S')
#
#    # now separate into lines
#    maze = maze_data.split()
#
#    # get start coordinates
#    start = (start % (len(maze[0]) + 1), start // len(maze[0]))
#
#    # get the maze as a graph
#    maze = get_maze(maze)
#
#    # find the furthest point in the maze
#    max_depth = 0
#    next_nodes = [(start, 0)]
#    
#    while next_nodes != []:
#        current, depth = next_nodes.pop(0)
#        max_depth = max(depth, max_depth)
#        for neighbour in maze[current]:
#            if neighbour != []:
#                next_nodes.append((neighbour, depth + 1))
#        maze[current] = []
#
#    # return answer
#    return max_depth


def colour_string(string, r, g, b):
    return f"\033[38;2;{r};{g};{b}m" + string + "\033[0m"

def bg_colour_string(string, r, g, b):
    return f"\033[48;2;{r};{g};{b}m" + string + "\033[0m"


if __name__ == "__main__":
    from sys import setrecursionlimit
    setrecursionlimit(100)
    with open("sample_1.txt") as maze_data:
        # get the start value
        maze_data = maze_data.read()
        print(maze_data)
        start = maze_data.index('S')
        maze = maze_data.split()
        start =  (start % (len(maze[0]) + 1), start // len(maze[0]))

        # get the maze as a dictionary
        maze = get_maze(maze)

        print(maze)

        # find the maximum distance along loops
        print(get_maximum_distance(start, maze, start, 0))
        # 6696 too low
