nums = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
}

def get_first_num(string):
    for i in range(len(string)):
        if string[i].isdigit():
            return string[i]
        for num in nums:
            if string[i:].startswith(num):
                return nums[num]

def get_last_num(string):
    for i in range(len(string)-1, -1, -1):
        if string[i].isdigit():
            return string[i]
        for num in nums:
            if string[:i+1].endswith(num):
                return nums[num]


def basic_calibration(data):
    total = 0
    for string in data:
        total += int(get_first_num(string) + get_last_num(string))
    return total


def advanced_calibration(data):
    total = 0
    for string in data:
        string = string.strip()
        total += int(get_first_num(string) + get_last_num(string))
    return total

if __name__ == '__main__':
    with open('sample_1.txt') as data:
        print(basic_calibration(data.readlines()))

    with open('input.txt') as data:
        print(advanced_calibration(data.readlines()))


