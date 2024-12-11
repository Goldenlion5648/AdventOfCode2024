from AoCLibrary import *
with open("input10.txt") as f:
    real_input = f.read()

def main(a : str, part2=False):
    a = a.strip()
    ret = 0
    board = read_grid(a, try_ints=True)
    starts = []
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == 0:
                starts.append(((y, x), 0, (y, x)))
    fringe = deque(starts)
    seen = {}
    while fringe:
        cur_pos, cur_val, origin = fringe.pop()
        if cur_val == 9:
            if part2:
                ret += 1
                continue
            else:
                key = (cur_pos, origin)
                if key in seen:
                    continue
                seen[key] = True
                ret += 1
                continue
        for dy, dx in adj:
            new = tuple(element_wise(cur_pos, (dy, dx)))
            if new[0] in range(len(board)) and new[1] in range(len(board[0])) and\
                board[new[0]][new[1]] == cur_val + 1:
                fringe.append((new, board[new[0]][new[1]], origin))
    return ret
    

ans(main(real_input))
ans(main(real_input, True))