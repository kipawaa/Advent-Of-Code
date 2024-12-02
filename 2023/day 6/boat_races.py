from math import sqrt, floor, ceil

def get_num_wins(races):
    # accumulator (since we are multiplying it starts at 1)
    num_ways_to_win = 1

    # for each race
    for time, record in races:
        # determine the winning values by finding the roots of the polynomial
        # in time holding down the button
        #       button_time (total_time - button_time) - (record + 1)
        # which is equivalent to 
        #       -button_time^2 - total_time button_time - (record + 1)
        # notice that button_time is actually our speed,
        # and total_time - button_time is how long we have to race after 
        # gathering our speed, so button_time (total_time - button_time)
        # represents the distance travelled.
        # we subtract record + 1, since we want to travel at least that far
        # to be sure that we win

        # get the roots
        sqrt_part = sqrt(time * time - 4 * (record + 1))
        left_root = (time - sqrt_part) / 2
        right_root = (time + sqrt_part) / 2

        # determine how many ways we can win this race
        num_ways_to_win_this_race = floor(right_root) - ceil(left_root) + 1

        # add to our product accumulator
        num_ways_to_win *= num_ways_to_win_this_race

    # return the answer
    return num_ways_to_win


if __name__ == "__main__":
    with open("input.txt") as data:
        user = int(input("problem 1 or 2?: "))
        if user == 1:
            races = data.readlines()
            races = zip([int(time) for time in races[0].split()[1:]],
                [int(record) for record in races[1].split()[1:]])

            print(get_num_wins(races))

        if user == 2:
            races = data.readlines()
            races = [(int(''.join(races[0].split()[1:])), 
                      int(''.join(races[1].split()[1:])))]
            print(races)
            print(get_num_wins(races))
