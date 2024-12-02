def is_safe_report(report):
    for i in range(1, len(report)):
        if not (1 <= abs(report[i] - report[i-1]) <= 3):
            return False
    return report == sorted(report) or report[::-1] == sorted(report)

def is_safe_dampened(report):
    for i in range(len(report)):
        if is_safe_report(report[:i] + report[i+1:]):
            return True
    return False

def p1(datafile="sample.txt"):
    with open(datafile, 'r') as data:
        num_safe_reports = 0
        for line in data:
            report = [int(level) for level in line.split()]
            if not is_safe_report(report):
                if is_safe_dampened(report):
                    num_safe_reports += 1
            else:
                num_safe_reports += 1


        print(num_safe_reports)

if __name__ == "__main__":
    p1(datafile="input.txt")
