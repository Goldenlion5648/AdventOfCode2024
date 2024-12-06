from AoCLibrary import *
with open("input6.txt") as f:
    real_input = f.read()

def main(a : str, part2=False):
    a = a.strip()
    inp = AdventInput(data=a)
    ret = 0
    board = inp.lines
    for i in range(len(inp.lines)):
        if inp.lines[i].find("^") != -1:
            y = i
            x = inp.lines[i].find("^")
            break
    def run(board, y, x):
        seen = set()
        dir = 0
        while True:
            new = (y, x)
            seen.add(new)
            dy, dx = directions[dir]
            if y +dy not in range(len(board)) or x + dx not in range(len(board[0])):
                break
            while board[y + dy][x + dx] == "#":
                dir += 1
                dir %= 4
                dy, dx = directions[dir]
            y += dy
            x += dx
            if y not in range(len(board)) or x not in range(len(board[0])):
                break
        return len(seen)

    def run2(board, y, x):
        seen = set()
        dir = 0
        while True:
            new = (y, x, dir)
            if new in seen:
                return True
            seen.add(new)
            dy, dx = directions[dir]
            if y +dy not in range(len(board)) or x + dx not in range(len(board[0])):
                break
            while board[y + dy][x + dx] == "#":
                dir += 1
                dir %= 4
                dy, dx = directions[dir]
            y += dy
            x += dx
            if y not in range(len(board)) or x not in range(len(board[0])):
                break
        return False

    if not part2:
        return run(board, y, x)
    board = lmap(list, board)
    for y2 in range(len(board)):
        for x2 in range(len(board[0])):
            if board[y2][x2] == ".":
                before = board[y2][x2]
                board[y2][x2] = "#"
                looped = run2(board, y, x)
                if looped:
                    ret += 1
                board[y2][x2] = before
    return ret

result = main(real_input)
if result is not None:
    ans(result)
result = main(real_input, True)
if result is not None:
    ans(result)