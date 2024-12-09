

def get_ordering(datafile="sample.txt"):
    ordering = {}
    
    with open(datafile, 'r') as data:
        line = data.readline()
        while line != '\n':
            left, right = line.split('|')
            if left not in ordering:
                ordering[left] = []
            ordering[left].append(right)
            data.readline()

    return ordering

def get_updates(datafile="sample.txt"):
    updates = []

    with open(datafile, 'r') as data:
        updates = data.readlines()

    return updates


def is_in_order(update, ordering):
    return update
