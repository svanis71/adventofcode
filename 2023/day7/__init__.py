from collections import Counter
from functools import cmp_to_key

from indata import read_list_of_strings


def get_hand(cards: str) -> int:
    hand_value = 1
    cnt = sorted(Counter(cards[:cards.index(' ')]).values(), reverse=True)
    if cnt[0] == 5:
        hand_value = 7
    elif cnt[0] == 4:
        hand_value = 6
    elif cnt[0] == 3 and cnt[1] == 2:
        hand_value = 5
    elif cnt[0] == 3:
        hand_value = 4
    elif cnt[0] == 2 == cnt[1]:
        hand_value = 3
    elif cnt[0] == 2:
        hand_value = 2
    return hand_value


def get_hand_with_joker(cards: str) -> int:
    card_counter = Counter(cards[:cards.index(' ')])
    jokers: int = card_counter['J'] if (card_counter['J'] == 0 or card_counter['J'] == 5) else card_counter.pop('J')
    cnt = sorted(card_counter.values(), reverse=True)
    hand_value: int = 1
    if cnt[0] == 5 or (jokers + cnt[0] == 5):
        hand_value = 7
    elif cnt[0] == 4 or (jokers + cnt[0] == 4):
        hand_value = 6
    elif (cnt[0] == 3 and cnt[1] == 2) or (cnt[0] >= 2 and (jokers + cnt[0] + cnt[1]) == 5):
        hand_value = 5
    elif cnt[0] == 3 or (jokers + cnt[0] == 3):
        hand_value = 4
    elif cnt[0] == 2 == cnt[1] or (jokers == 1 and cnt[0] == 2):
        hand_value = 3
    elif cnt[0] == 2 or 'J' in cards:
        hand_value = 2
    return hand_value


def compare_hands(h1, h2, cardrank: str, use_joker: bool = False):
    hand1 = get_hand(h1) if not use_joker else get_hand_with_joker(h1)
    hand2 = get_hand(h2) if not use_joker else get_hand_with_joker(h2)

    if hand1 > hand2:
        return 1
    if hand1 < hand2:
        return -1
    cardrank = {c: ix for ix, c in enumerate(cardrank)}
    for c1, c2 in zip(h1, h2):
        if cardrank[c1] == cardrank[c2]:
            continue
        return 1 if cardrank[c1] > cardrank[c2] else -1
    return 0


def part1():
    def _compare_hands(h1: str, h2: str) -> int:
        return compare_hands(h1, h2, "23456789TJQKA")

    indata = read_list_of_strings('day7', use_testdata=False)
    sorted_hands = sorted(indata, key=cmp_to_key(_compare_hands))
    return sum((ix * int(hand.split(' ')[1])) for ix, hand in enumerate(sorted_hands, 1))


def part2():
    def _compare_hands(h1: str, h2: str) -> int:
        return compare_hands(h1, h2, "J23456789TQKA", True)

    indata = read_list_of_strings('day7', use_testdata=False)
    sorted_hands = sorted(indata, key=cmp_to_key(_compare_hands))
    return sum((ix * int(hand.split(' ')[1])) for ix, hand in enumerate(sorted_hands, 1))


def run():
    print(f'Day 7 pt1: {part1()}')
    print(f'Day 7 pt2: {part2()}')

# Day 7 pt1: 246163188
# Day 7 pt2: 245794069
