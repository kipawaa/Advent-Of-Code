def get_min_location(almanac):
    seeds = [int(s) for s in almanac[0].split()[1:]]
    
    # for each type of mapping
    print(f"start: {seeds}")
    i = 1
    for _ in range(8):
        mapped_seeds = [seed for seed in seeds]
        while i < len(almanac) and almanac[i] != '\n':
            dest, source, length = [int(val) for val in almanac[i].split()]
            for s in range(len(seeds)):
                if source <= seeds[s] < source + length:
                    mapped_seeds[s] = dest + (seeds[s] - source)
                    print(f"{seeds[s]} -> {mapped_seeds[s]}")
            i += 1
        seeds = mapped_seeds
        print(seeds)
        i += 2

    return min(seeds)


def get_min_location_from_range(almanac):
    # get data
    vals = almanac[0].strip().split()[1:]

    # get initial ranges
    seed_ranges = [(int(vals[i]), int(vals[i+1])) for i in range(0, len(vals), 2)]

    print(f"starting with seed ranges {seed_ranges}")
    
    # for each set of maps
    for _ in range(8):
        # for each seed
        for seed_range in seed_ranges:
            # apply the maps
            while i < len(almanac) and almanac[i] != '\n':

                # progress
                i += 1

    # get the min


if __name__ == "__main__":
    with open("sample.txt") as data_file:
        data = data_file.readlines()
        #print(f"result: {get_min_location(data)}")
        print(f"result: {get_min_location_from_range(data)}")
