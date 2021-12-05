class Board:
    def __init__(self, board):
        self.board = board
        self.pivot_board = [[], [], [], [], []]
        for y in range(0, 5):
            for x in range(0, 5):
                self.pivot_board[y].append(board[x][y])

    def score(self, drawn_numbers):
        for y in range(0, 5):
            if set(self.board[y]).issubset(drawn_numbers) or set(self.pivot_board[y]).issubset(drawn_numbers):
                # self.bingo(drawn_numbers)
                return sum([sum(set(x for x in line).difference(drawn_numbers)) for line in self.board]) * \
                       drawn_numbers[0]
        return 0

    def bingo(self, drawn_numbers):
        print(f'Bingo! Last number was {drawn_numbers[0]}')
        for line in self.board:
            for num in line:
                if num in drawn_numbers:
                    print(f' \033[94m\033[1m{num:2}\033[0m', end='')
                else:
                    print(f' {num:2}', end='')
            print()


def create_bingo_game():
    boards = []
    with open('indata/day4.txt') as f:
        bingo_numbers = [int(num) for num in f.readline().strip().split(',')]
        while f.readline():
            board = []
            for i in range(0, 5):
                board.append([int(s) for s in f.readline().strip().replace('  ', ' ').split(' ')])
            b = Board(board)
            boards.append(b)
    return boards, bingo_numbers


def part1():
    boards, bingo_numbers = create_bingo_game()
    drawn_numbers = []
    for number in bingo_numbers:
        drawn_numbers.insert(0, number)
        for board in boards:
            score = board.score(drawn_numbers)
            if score > 0:
                return score
    return 0


def part2():
    boards, bingo_numbers = create_bingo_game()
    drawn_numbers = []
    winners = []
    for number in bingo_numbers:
        drawn_numbers.insert(0, number)
        for ix, board in enumerate(boards):
            score = board.score(drawn_numbers)
            if score > 0:
                winners.insert(0, score)
                boards.pop(ix)

    return winners[0]


def run():
    print(f'Day 4 pt1: {part1()}')
    print(f'Day 4 pt2: {part2()}')

# Day 4 pt1: 25410
# Day 4 pt2: 2730
