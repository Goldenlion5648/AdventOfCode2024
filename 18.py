from AoCLibrary import *
with open("input18.txt") as f:
    real_input = f.read()

def main(a : str, is_part2):
    a = a.strip()
    y_dim = 71
    x_dim = 71
    lines_shown = 1024
    board = dd(lambda : ".")
    all_lines = lines(a)
    for y in range(y_dim):
        board[y, -1] = "#"
        board[y, x_dim] = "#"
    for x in range(x_dim):
        board[-1, x] = "#"
        board[y_dim, x] = "#"

    for i, line in enu(all_lines):
        if i >= lines_shown:
            break
        x, y = nums(line)
        board[y, x] = "#"

    def search(board):
        fringe = deque([((0, 0), 0)])
        seen = set()
        goal = (y_dim - 1, x_dim - 1)
        while fringe:
            cur, steps = fringe.popleft()
            if cur == goal:
                return steps
            if cur in seen:
                continue
            seen.add(cur)
            for offset in adj:
                new = element_wise_tup(cur, offset)
                if board[new] != "#":
                    fringe.append((new, steps + 1))
        return -1

    if not is_part2:
        return search(board)

    for i in range(lines_shown, len(all_lines)):
        line = all_lines[i]
        x, y = nums(line)
        board[y, x] = "#"
        steps_to_exit = search(board)
        if steps_to_exit == -1:
            return line

ans(main(real_input, False))
ans(main(real_input, True))