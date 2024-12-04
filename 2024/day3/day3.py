import re

def sol(datafile="input.txt"):

    p1pattern = r"mul\(\d{1,3},\d{1,3}\)"
    p2pattern = r"((?:\A|do\(\))(?:\s|.)*?(?:don't\(\)|\Z))"

    with open(datafile, 'r') as data:
        data = data.read()
        
        total = 0

        valid_regions = re.findall(p2pattern, data, flags=re.M)
        for region in valid_regions:
            print(region)
            for mul in re.findall(p1pattern, region):
                left, right = mul[4:-1].split(",")
                total += int(left) * int(right)

        print(total)

if __name__ == "__main__":
    sol()
