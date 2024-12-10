def p1(datafile="sample.txt"):
    with open(datafile, 'r') as data:
        order = {}

        line = data.readline()

        while line != '\n':
            first, last = map(int, line.split('|'))
            if first not in order:
                order[first] = []
            order[first].append(last)
            line = data.readline()

        print(order)

        total = 0
    
        for line in data:
            nums = [int(num) for num in line.strip().split(',')]
            if is_ordered(nums, order):
                print(f"{nums} is in order")
                print(f"\tadding {nums[len(nums) // 2]}")
                total += int(nums[len(nums) // 2])
            else:
                print(f"{nums} is not in order")

    return total


def is_ordered(nums, order):
    for i in range(len(nums)):
        for num in nums[:i]:
            if nums[i] in order and num in order[nums[i]]:
                return False

    return True


if __name__ == "__main__":
    print(p1(datafile="input.txt"))
