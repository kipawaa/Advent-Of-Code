"""
--- Day 10: Pipe Maze ---
You use the hang glider to ride the hot air from Desert Island all the way up
to the floating metal island. This island is surprisingly cold and there
definitely aren't any thermals to glide on, so you leave your hang glider
behind.

You wander around for a while, but you don't find any people or animals.
However, you do occasionally find signposts labeled "Hot Springs" pointing in a
seemingly consistent direction; maybe you can find someone at the hot springs
and ask them where the desert-machine parts are made.

The landscape here is alien; even the flowers and trees are made of metal. As
you stop to admire some metal grass, you notice something metallic scurry away
in your peripheral vision and jump into a big pipe! It didn't look like any
animal you've ever seen; if you want a better look, you'll need to get ahead of
it.

Scanning the area, you discover that the entire field you're standing on is
densely packed with pipes; it was hard to tell at first because they're the
same metallic silver color as the "ground". You make a quick sketch of all of
the surface pipes you can see (your puzzle input).

The pipes are arranged in a two-dimensional grid of tiles:

| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but
your sketch doesn't show what shape the pipe has.
Based on the acoustics of the animal's scurrying, you're confident the pipe
that contains the animal is one large, continuous loop.

For example, here is a square loop of pipe:

.....
.F-7.
.|.|.
.L-J.
.....
If the animal had entered this loop in the northwest corner, the sketch would
instead look like this:

.....
.S-7.
.|.|.
.L-J.
.....
In the above diagram, the S tile is still a 90-degree F bend: you can tell
because of how the adjacent pipes connect to it.

Unfortunately, there are also many pipes that aren't connected to the loop!
This sketch shows the same loop as above:

-L|F7
7S-7|
L|7||
-L-J|
L|-JF
In the above diagram, you can still figure out which pipes form the main loop:
they're the ones connected to S, pipes those pipes connect to, pipes those
pipes connect to, and so on. Every pipe in the main loop connects to its two
neighbors (including S, which will have exactly two pipes connecting to it, and
which is assumed to connect back to those two pipes).

Here is a sketch that contains a slightly more complex main loop:

..F7.
.FJ|.
SJ.L7
|F--J
LJ...
Here's the same example sketch with the extra, non-main-loop pipe tiles also
shown:

7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
If you want to get out ahead of the animal, you should find the tile in the
loop that is farthest from the starting position. Because the animal is in the
pipe, it doesn't make sense to measure this by direct distance. Instead, you
need to find the tile that would take the longest number of steps along the
loop to reach from the starting point - regardless of which way around the loop
the animal went.

In the first example with the square loop:

.....
.S-7.
.|.|.
.L-J.
.....
You can count the distance each tile in the loop is from the starting point
like this:

.....
.012.
.1.3.
.234.
.....
In this example, the farthest point from the start is 4 steps away.

Here's the more complex loop again:

..F7.
.FJ|.
SJ.L7
|F--J
LJ...
Here are the distances for each tile on that loop:

..45.
.236.
01.78
14567
23...
Find the single giant loop starting at S. How many steps along the loop does it
take to get from the starting position to the point farthest from the starting
position?
"""


def get_maze(maze_data):
    graph = {(x,y): [] for x in range(len(maze_data[0])) for y in range(len(maze_data))}
    for y in range(len(maze_data)):
        for x in range(len(maze_data[y])):
            match maze_data[y][x]:
                case '|':
                    if y > 0:
                        graph[(x,y-1)].append((x,y))
                        graph[(x,y)].append((x,y-1))
                    if y < len(maze_data) -1:
                        graph[(x,y)].append((x,y+1))
                        graph[(x,y+1)].append((x,y))
                case '-':
                    if x > 0:
                        graph[(x-1,y)].append((x,y))
                        graph[(x,y)].append((x-1,y))
                    if x < len(maze_data[y]) - 1:
                        graph[(x,y)].append((x+1,y))
                        graph[(x+1,y)].append((x,y))
                case 'L':
                    if y > 0:
                        graph[(x,y-1)].append((x,y))
                        graph[(x,y)].append((x,y-1))
                    if x < len(maze_data[y]):
                        graph[(x,y)].append((x+1,y))
                        graph[(x+1,y)].append((x,y))
                case 'J':
                    if y > 0:
                        graph[(x,y-1)].append((x,y))
                        graph[(x,y)].append((x,y-1))
                    if x > 0:
                        graph[(x,y)].append((x-1,y))
                        graph[(x-1,y)].append((x,y))
                case '7':
                    if x > 0:
                        graph[(x-1,y)].append((x,y))
                        graph[(x,y)].append((x-1,y))
                    if y < len(maze_data) - 1:
                        graph[(x,y)].append((x,y+1))
                        graph[(x,y+1)].append((x,y))
                case 'F':
                    if x < len(maze_data[y]) - 1:
                        graph[(x+1,y)].append((x,y))
                        graph[(x,y)].append((x+1,y))
                    if y < len(maze_data) - 1:
                        graph[(x,y)].append((x,y+1))
                        graph[(x,y+1)].append((x,y))
                case _:
                    pass
    return graph
            


def get_maximum_distance(maze_data):
    # read rather than readlines so that we can find start easily
    maze = maze_data.read()
    start = maze.index('S')

    # now separate into lines
    maze = maze.split()

    # get start coordinates
    start = (start % len(maze[0]), start // len(maze[0]))

    # get the maze as a graph
    maze = get_maze(maze)

    # find the furthest point in the maze
    


if __name__ == "__main__":
    with open("sample_1-1.txt") as maze_data:
        print(get_maximum_distance(maze_data))
