def get_difference_sequence(sequence):
    diffs = []
    for i in range(len(sequence) - 1):
        diffs.append(sequence[i+1] - sequence[i])
    return diffs


def sum_forward_extrapolations(sequences):
    sequences = [[int(i) for i in sequence.split()] for sequence in sequences]
    total = 0
    for sequence in sequences:
        diffs = [sequence]
        while sum(diffs[-1]) != 0:
            diffs.append(get_difference_sequence(diffs[-1]))
        
        diffs[-1].append(0)
        for i in range(len(diffs)-2, -1, -1):
            diffs[i].append(diffs[i+1][-1] + diffs[i][-1])
        
        total += diffs[0][-1]
    return total


def sum_backward_extrapolations(sequences):
    sequences = [[int(i) for i in sequence.split()] for sequence in sequences]
    total = 0
    for sequence in sequences:
        diffs = [sequence]
        while sum(diffs[-1]) != 0:
            diffs.append(get_difference_sequence(diffs[-1]))
        
        diffs[-1].insert(0, 0)
        for i in range(len(diffs)-2, -1, -1):
            diffs[i].insert(0, diffs[i][0] - diffs[i+1][0])
        
        total += diffs[0][0]
    return total

if __name__ == "__main__":
    with open("input.txt") as data:
        print(sum_backward_extrapolations(data))
