def has_guard(grid):
    for row in grid:
        if '>' in row or '<' in row or '^' in row or 'v' in row:
            return True

    return False


def get_guard_pos_and_state(grid):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] in ('<', '>', '^', 'v'):
                return (r, c, grid[r][c])
    return (-1,-1, '')


def will_hit_obstacle(pos, state, grid):
    r, c = pos
    
    if state == '>' and c < len(grid[r]) - 1 and grid[r][c+1] == '#':
        return True

    if state == '<' and c > 0 and grid[r][c-1] == '#':
        return True

    if state == '^' and r > 0 and grid[r-1][c] == '#':
        return True

    if state == 'v' and r < len(grid) - 1 and grid[r+1][c] == '#':
        return True

    return False


def get_next_state(state):
    if state == '>':
        return 'v'

    if state == 'v':
        return '<'

    if state == '<':
        return '^'

    if state == '^':
        return '>'


def step(grid):
    r, c, state = get_guard_pos_and_state(grid)

    if will_hit_obstacle((r, c), state, grid):
        state = get_next_state(state)
    
    if state == '>' and c < len(grid[r]) - 1:
            grid[r][c+1] = '>'

    if state == 'v' and r < len(grid) - 1:
            grid[r+1][c] = 'v'

    if state == '<' and c > 0:
        grid[r][c-1] = '<'

    if state == '^' and r > 0:
        grid[r-1][c] = '^'

    grid[r][c] = 'X'

    return grid


def count_positions(grid):
    total = 0

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            total += grid[r][c] == 'X'

    return total



def printgrid(grid):
    out = ""
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            out += grid[r][c]
        out += '\n'

    print(out)


def p1(datafile="sample.txt"):
    grid = []

    with open(datafile, 'r') as data:
        for line in data:
            grid.append([c for c in line])

    printgrid(grid)

    while has_guard(grid):
        grid = step(grid)


    printgrid(grid)

    print(count_positions(grid))


if __name__ == "__main__":
    p1(datafile="input.txt")
