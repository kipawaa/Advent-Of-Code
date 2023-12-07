def get_num_winners(card):
    winning_nums, elf_nums = card.split('|')
    winning_nums = winning_nums.strip().split()
    elf_nums = elf_nums.strip().split()
    return sum([1 if num in winning_nums else 0 for num in elf_nums]) 

def get_points(card):
    return 2 ** (get_num_winners(card) - 1)


def get_total_points(cards):
    total = 0
    for card in cards:
        value = get_points(card.split(':')[1].strip())
        if value >= 1:
            total += value

    return total


def get_num_scratchcards(cards):
    # keep track of how many of each card we have
    num_cards = [1 for i in range(len(cards))]

    # for each card
    for i in range(len(cards)):
        # figure out our winning numbers
        card_num, nums = cards[i].split(':')
        num_wins = get_num_winners(nums)

        # for each of our winning numbers
        for j in range(1, num_wins+1):
            # add a copy of the next cards for each copy of this card
            num_cards[i + j] += num_cards[i]

    return sum(num_cards)


if __name__ == "__main__":
    with open("input.txt") as data:
        print(get_total_points(data.readlines()))

    with open("input.txt") as data:
        print(get_num_scratchcards(data.readlines()))
