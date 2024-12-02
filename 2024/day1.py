def dist(x, y):
    return abs(x - y)

def list_dist(l1, l2):
    d = 0
    for i in range(len(l1)):
        d += dist(l1[i], l2[i])

    return d

def get_lists(data):
    l1, l2 = [], []
    for line in data:
        d1,d2 = line.split()
        l1.append(int(d1))
        l2.append(int(d2))

    return (l1, l2)

def p1(datafile="sample.txt"):
    with open(datafile, 'r') as data:
        l1, l2 = get_lists(data)

        l1.sort()
        l2.sort()

        print(list_dist(l1, l2))

def p2(datafile="sample.txt"):
    with open(datafile, 'r') as data:
        l1, l2 = get_lists(data)

        similarity = 0
        for num in l1:
            similarity += num * l2.count(num)

        print(similarity)


if __name__ == "__main__":
    p1(datafile="input.txt")
    p2(datafile="input.txt")
