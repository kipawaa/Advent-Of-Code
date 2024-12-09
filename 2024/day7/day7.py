def can_be_valid(equation, operators):
    value, operands = equation.strip().split(': ')
    
    value = int(value)
    operands = [int(val) for val in operands.split()]

    return value if value in get_possible_values(operands, operators) else 0

def get_possible_values(operands, operators):
    if len(operands) == 1:
        return operands

    possible_values = []
    for operator in operators:
        possible_values += get_possible_values([operator(operands[0], operands[1])] + operands[2:], operators)

    return possible_values
    

def get_total_calibration(datafile="sample.txt"):
    operators = [lambda x,y: x + y, lambda x,y: x * y, lambda x,y: int(str(x) + str(y))]
    with open(datafile, 'r') as data:
        total = 0
        for equation in data:
            total += can_be_valid(equation, operators)

        return total


if __name__ == "__main__":
    print(get_total_calibration(datafile="input.txt"))
