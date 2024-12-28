def p1(datafile="sample.txt"):
    with open(datafile, 'r') as data:
        order = get_order(data)

        print(order)

        total = 0
    
        for line in data:
            nums = [int(num) for num in line.strip().split(',')]
            if is_ordered(nums, order):
                total += int(nums[len(nums) // 2])

    return total


def get_order(data):
    """
    return a dictionary with keys that must occur before any of their values

    data: open file with order data
    """
    order = {}
    line = data.readline()
    while line != '\n':
        first, last = map(int, line.split('|'))
        if first not in order:
            order[first] = []
        order[first].append(last)
        line = data.readline()

    return order


def is_ordered(nums, order):
    for i in range(len(nums)):
        for num in nums[:i]:
            if nums[i] in order and num in order[nums[i]]:
                return False

    return True


def p2(datafile="sample.txt"):
    with open(datafile, 'r') as data:
        order = get_order(data)

        total = 0

        for line in data:
            nums = [int(num) for num in line.strip().split(',')]
            if not is_ordered(nums, order):
                correct_nums = correct_order(nums, order)
                print(f"ordered {nums} as {correct_nums}")
                val = int(correct_nums[len(correct_nums) // 2])
                print(f"adding {val}")
                total += val
    
    return total


def correct_order(given_nums, order):
    nums = [num for num in given_nums]
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] in order and nums[j] in order[nums[i]]:
                nums[i], nums[j] = nums[j], nums[i]

    return nums
    

if __name__ == "__main__":
    print(p2(datafile="input.txt"))
    #print(p1(datafile="input.txt"))
