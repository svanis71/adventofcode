from indata import read_list_of_strings


def solution() -> tuple[int, int]:
    cards: list[str] = read_list_of_strings('day4', use_testdata=False)
    points: list[int] = []
    copies: dict = {cardno: 1 for cardno, _ in enumerate(cards, 1)}
    for cardno, card in enumerate(cards, 1):
        washed: str = card[card.find(':') + 2:]
        list_of_winning_numbers, numbers_on_hand = washed.replace('  ', ' ').strip().split(' | ')
        winning_numbers: list[int] = [int(n) for n in list_of_winning_numbers.split(' ')]
        my_numbers: list[int] = [int(n) for n in numbers_on_hand.split(' ')]
        winners: list[int] = [wn for wn in my_numbers if wn in winning_numbers]
        matching_numbers: int = len(winners)
        if matching_numbers > 0:
            points.append(2 ** (matching_numbers - 1))
            for i in range(cardno + 1, cardno + matching_numbers + 1):
                copies[i] += copies[cardno]
    return sum(points), sum(copies.values())


def run():
    p1, p2 = solution()
    print(f'Day 4 pt1: {p1}')
    print(f'Day 4 pt2: {p2}')

# Day 4 pt1:
# Day 4 pt2:
