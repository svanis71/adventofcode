from indata import read_list_of_strings


def part1():
    moves = [d.split(' ') for d in read_list_of_strings('day9')]
    head_pos, tail_pos = {"x": 0, "y": 0}, {"x": 0, "y": 0}
    head_path, tail_path = [(head_pos["x"], head_pos["y"])], [(tail_pos["x"], tail_pos["y"])]
    for dir, steps in moves:
        for _ in range(int(steps)):
            # URLD
            match dir:
                case 'U':
                    head_pos["y"] -= 1
                    if tail_pos["y"] > head_pos["y"] + 1:
                        tail_pos["y"] -= 1
                        if tail_pos["x"] != head_pos["x"]:
                            tail_pos["x"] = head_pos["x"]
                case 'D':
                    head_pos["y"] += 1
                    if tail_pos["y"] < head_pos["y"] - 1:
                        tail_pos["y"] += 1
                        if tail_pos["x"] != head_pos["x"]:
                            tail_pos["x"] = head_pos["x"]
                case 'L':
                    head_pos["x"] -= 1
                    if tail_pos["x"] > head_pos["x"] + 1:
                        tail_pos["x"] -= 1
                        if tail_pos["y"] != head_pos["y"]:
                            tail_pos["y"] = head_pos["y"]
                case 'R':
                    head_pos["x"] += 1
                    if tail_pos["x"] < head_pos["x"] - 1:
                        tail_pos["x"] += 1
                        if tail_pos["y"] != head_pos["y"]:
                            tail_pos["y"] = head_pos["y"]
            tail_path.append((tail_pos["x"], tail_pos["y"]))
            head_path.append((head_pos["x"], head_pos["y"]))
    return len(set(tail_path))


def part2():
    moves = [d.split(' ') for d in read_list_of_strings('day9', is_testdata=True)]
    head_pos, head_path = {"x": 0, "y": 0}, [(0, 0)]
    tail, tailpath = [{"x": 0, "y": 0} for _ in range(10)], [(0, 0) for _ in range(10)]
    for dir, steps in moves:
        for _ in range(int(steps)):
            # URLD
            match dir:
                case 'U':
                    head_pos["y"] -= 1
                case 'D':
                    head_pos["y"] += 1
                case 'L':
                    head_pos["x"] -= 1
                case 'R':
                    head_pos["x"] += 1
            hx, hy = head_pos["x"], head_pos["y"]
            for tailidx, t in enumerate(tail):
                tx, ty = t["x"], t["y"]
                if tailidx == 0: # closest to head
                    if ty > hy + 1: # up
                        ty -= 1
                        tx = hx if tx != hx else tx
                    if ty < hy - 1: # down
                        ty += 1
                        tx = hx if tx != hx else tx
                    if tx > hx + 1: # left
                        tx -= 1
                        ty = hy if ty != hy else ty
                    if tx < hx - 1: # right
                        tx += 1
                        ty = hy if ty != hy else ty
                else:
                    tx_prev, ty_prev = tail[tailidx - 1]["x"], tail[tailidx - 1]["y"]
                    if ty > ty_prev + 1:  # up
                        ty -= 1
                        tx = tx_prev if tx != tx_prev else tx
                    if ty < ty_prev - 1:  # down
                        ty += 1
                        tx = tx_prev if tx != tx_prev else tx
                    if tx > tx_prev + 1:  # left
                        tx -= 1
                        ty = ty_prev if ty != ty_prev else ty
                    if tx < tx_prev - 1:  # right
                        tx += 1
                        ty = ty_prev if ty != ty_prev else ty

                tail[tailidx]["x"] = tx
                tail[tailidx]["y"] = ty
            tailpath.append((tail[9]["x"], tail[9]["y"]))

    return len(set(tailpath))

def run():
    print(f'Day 9 pt1: {part1()}')
    print(f'Day 9 pt2: {part2()}')

# Day 9 pt1:
# Day 9 pt2:
