value_dict = {
        'A': 'Z',
        'K': 'Y',
        'Q': 'X',
        'J': 'W',
        'T': 'V'
}

wildcard_dict = {
        'A': 'Z',
        'K': 'Y',
        'Q': 'X',
        'J': '0',
        'T': 'V'
}


def grade_hand(handbid, has_wildcards):
    # get the hand from the hand-bid pair
    hand = handbid[0]

    # determine which dictionary we're using based on presence of wildcards
    # (task 1 vs task 2)
    card_values = wildcard_dict if has_wildcards else value_dict
    
    # annoying case of all wildcards
    if hand == 'JJJJJ':
            return '7' + 5 * card_values['J']


    # the best hand is the one that uses the wildcards as copies of the
    # card that occurs most in the hand, so we can simply make all of the
    # wildcards into that card

    # find the card that occurs the most
    most_occurring = sorted(hand.replace('J', '') if has_wildcards else hand, key=lambda x : str(hand.count(x)))[-1]
    
    # replace wildcards with most occurring card
    scoring_hand = ''.join([most_occurring if i == 'J' else i for i in hand]) if has_wildcards else hand

    # determine how many times the most-occurring card occurs
    num_occurrences = scoring_hand.count(most_occurring)

    # re-label the cards in the hand so that we can sort them as strings
    hand = ''.join([i if i in '23456789' else card_values[i] for i in hand])

    #TODO this could probably be reduced to a single return
    match num_occurrences:
        # five of a kind
        case 5:
            return '7' + hand

        # four of a kind
        case 4:
            return '6' + hand

        # three of the most occurring card is one of two things:
        case 3:
            # full house
            if len(set(scoring_hand)) == 2:
                return '5' + hand

            # three of a kind
            return '4' + hand

        # pair(s)
        case 2:
            # two pair
            if len(set(scoring_hand)) == 3:
                return '3' + hand

            # pair
            return '2' + hand

        # high card
        case _:
            return '1' + hand


def get_total_winnings(game, has_wildcards):
    ranks = sorted(game, key=lambda x : grade_hand(x, has_wildcards))

    winnings = 0
    for i in range(len(ranks)):
        winnings += int(ranks[i][1]) * (i + 1)
        print(ranks[i], i+1, winnings)

    return winnings

if __name__ == "__main__":
    with open("input.txt") as data:
        game = [line.split() for line in data.readlines()]
        print(get_total_winnings(game, True))

        # 245 714 840 is too low
        # 245 899 795 is too high
