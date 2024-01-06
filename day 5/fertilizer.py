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

    # for each mapping
    i = 3
    for _ in range(8):
        #print(f"new almanac map, ranges are {seed_ranges}")
        # get the new mapped seeds
        mapped_seed_ranges = []

        # for each entry for this map
        while i < len(almanac) and almanac[i] != '\n':
            # get the mapping on this line
            dest, source, length = [int(val) for val in almanac[i].split()]
            diff = dest - source

            print(f"mapping: {source} -> {dest} with length {length}")
            
            # keep track of the things that don't get mapped so that we can carry them along as well
            unmapped_seed_indices = [i for i in range(len(seed_ranges))]

            # for each of the ranges we have
            for s in range(len(seed_ranges)):

                print(f"\tchecking range {seed_ranges[s]}")

                # if this mapping range falls inside the seed range
                if seed_ranges[s][0] <= source <= seed_ranges[s][0] + seed_ranges[s][1]:
                    # preserve the unmapped part of the interval
                    if seed_ranges[s][0] != source:
                        # this could still be mapped by some part of this section of the almanac,
                        # so we need to keep it in seed_ranges
                        seed_ranges[s] = (seed_ranges[s][0], source - seed_ranges[s][0])

                    # map the part of the interval that lies in the mapped portion
                    if seed_ranges[s][1] <= source + length:
                        mapped_seed_ranges.append((source + diff, seed_ranges[s][1] + diff))
                    else:
                        mapped_seed_ranges.append((source + diff, source + length-1 + diff))
                        mapped_seed_ranges.append((source + length, seed_ranges[s][1]))
                    
                    print("\tmapped something that contains the map")
                    
                    unmapped_seed_indices.remove(s)

                # if the seed range falls in the mapping range
                elif source <= seed_ranges[s][0] <= source + length:
                    # if the whole range falls inside the mapping
                    if seed_ranges[s][1] < source + length:
                        mapped_seed_ranges.append((seed_ranges[s][0] + diff, seed_ranges[s][1] + diff))
                    else:
                        mapped_seed_ranges.append((seed_ranges[s][0] + diff, source + length-1 + diff))
                        mapped_seed_ranges.append((source + length, seed_ranges[s][1]))
                    
                    print("\tmapped something that is contained in the map")
                    
                    unmapped_seed_indices.remove(s)
            i += 1

        # carry along the things that didn't get mapped
        for i in unmapped_seed_indices:
            mapped_seed_ranges.append(seed_ranges[i])

        print(f"mapped seeds at end of run: {mapped_seed_ranges}")
        
        # the mapped seeds are the new old seeds for the next mapping
        seed_ranges = mapped_seed_ranges

        # jump to the next entry in the almanac
        i += 2
    
    # get the answer!
    return min(seed_ranges, key=lambda x : x[0])[0]


if __name__ == "__main__":
    with open("sample.txt") as data_file:
        data = data_file.readlines()
        #print(f"result: {get_min_location(data)}")
        print(f"result: {get_min_location_from_range(data)}")
