def build_maps(almanac):
    maps = {
        'seed_to_soil': {},
        'soil_to_fertilizer': {},
        'fertilizer_to_water': {},
        'water_to_light': {},
        'light_to_temperature': {},
        'temperature_to_humidity': {},
        'humidity_to_location': {}
    }

    l = 3
    for key in maps:
        while l < len(almanac) and almanac[l] != '\n':
            dest, source, length = [int(val) for val in almanac[l].split()]
            for i in range(length):
                maps[key][source + i] = dest + i

            l += 1
        l += 2

    return maps
        
def get_locations(almanac, seeds):
    seeds = [int(s) for s in seeds]
    # for each type of mapping
    print(f"start: {seeds}")
    i = 0
    for _ in range(8):
        mapped_seeds = seeds
        while i < len(almanac) and almanac[i] != '\n':
            dest, source, length = [int(val) for val in almanac[i].split()]
            for s in range(len(seeds)):
                if source <= seeds[s] < source + length:
                    print(almanac[i])
                    mapped_seeds[s] = dest + (seeds[s] - source)
                    print(seeds)
            i += 1
        seeds = mapped_seeds
        i += 2

    return seeds


if __name__ == "__main__":
    with open("input.txt") as data_file:
        data = data_file.readlines()
        print(f"result: {min(get_locations(data[1:], [int(val) for val in data[0].split()[1:]]))}")
