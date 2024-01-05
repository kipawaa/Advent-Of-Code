def sum_engine_parts(engine_lines):
    # clean the lines and make them a grid
    # we add an extra '.' at the end of each line since we are using
    # if ... else and resetting after each line, meaning that
    # part numbers at the end of a line will trigger the if part
    # and not get totalled since that requires the else
    engine = [line.strip() + '.' for line in engine_lines]

    # accumulate the part numbers
    total = 0

    # for each character in engine
    for i in range(len(engine)):
        # accumulate the part numbers as we go
        num = ''

        # keep a flag so we know if they're included or not
        isPart = False

        # loop over the grid and total things!
        for j in range(len(engine[i])):
            # if we find a number then accumulate it
            if engine[i][j].isdigit():
                num += engine[i][j]

                # if we haven't already found a symbol next to this number then
                # check for one
                if not isPart:
                    for y in (-1, 0, 1):
                        for x in (-1, 0, 1):
                            # make sure we don't run off the grid
                            if 0 <= i + y < len(engine) and \
                               0 <= j + x < len(engine[i]) \
                               and engine[i + y][j + x] not in '0123456789.':
                                isPart = True
            else:
                # if we found the end of a valid part number then
                # add it to our total
                if num != '' and isPart:
                    total += int(num)

                # reset our number and part status
                isPart = False
                num = ''

    # send back the answer
    return total


def sum_gear_ratios(engine_lines):
    # clean the lines and make them a grid
    engine = [line.strip() for line in engine_lines]

    # accumulate the gear ratios
    total = 0

    # loop over the engine characters
    for i in range(len(engine)):
        for j in range(len(engine[i])):
            # if we find a gear
            if engine[i][j] == '*':
                # accumulate adjacent part numbers
                adjacent_parts = []

                # check for adjacent part numbers
                for y in (-1, 0, 1):
                    for x in (-1, 0, 1):
                        # if we find a number then get the rest of it
                        if engine[i + y][j + x].isdigit():
                            

    # send back the answer
    return total


if __name__ == "__main__":
    with open("input.txt") as data:
        print(sum_engine_parts(data.readlines()))

    with open("sample_1.txt") as data:
        print(sum_gear_ratios(data.readlines()))
