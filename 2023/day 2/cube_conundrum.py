MAXRED = 12
MAXGREEN = 13
MAXBLUE = 14

COLOURS = ['red', 'blue', 'green']

def get_max_cubes_from_sets(sets):
    maxes = {colour : 0 for colour in COLOURS}
    for s in sets:
        s = s.strip().split(',')
        for blocks in s:
            num, colour = blocks.split()
            maxes[colour] = max(int(num), maxes[colour])
    return maxes


def is_valid_game(gamestring):
    gamestring = gamestring.strip().split(':')
    sets = gamestring[1].strip().split(';')

    maxes = get_max_cubes_from_sets(sets)

    return maxes['red'] <= MAXRED and maxes['blue'] <= MAXBLUE and maxes['green'] <= MAXGREEN


def sum_valid_game_ids(games):
    total = 0
    for game in games:
        if is_valid_game(game):
            total += int(game[5:game.index(':')])
    return total


def sum_powers_of_cubes(games):
    total = 0
    for game in games:
        game = game.split(':')[1].strip()
        print(game)
        maxes = get_max_cubes_from_sets(game.split(';'))
        total += maxes['red'] * maxes['green'] * maxes['blue']
    return total

if __name__ == "__main__":
    with open('sample_1.txt') as games:
        print(sum_valid_game_ids(games.readlines()))

    with open('input.txt') as games:
        print(sum_powers_of_cubes(games.readlines()))
