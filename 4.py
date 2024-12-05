from AoCLibrary import *
with open("input4.txt") as f:
    real_input = f.read()

def main(a : str, part2=False):
    a = a.strip()
    board = lines(a)

    def normal_search(board):
        ret = 0
        word = "XMAS"
        for y in range(len(board)):
            for x in range(len(board[0])):
                good = True
                for i in range(len(word)):
                    if x + i >= len(board[y]) or board[y][x + i] != word[i]:
                        good = False
                        break
                if good:
                    ret += 1
        for y in range(len(board)):
            for x in range(len(board[0])):
                good = True
                for i in range(len(word)):
                    if x - i < 0 or board[y][x - i] != word[i]:
                        good = False
                        break
                if good:
                    ret += 1

        for y in range(len(board)):
            for x in range(len(board[0])):
                good = True
                for i in range(len(word)):
                    if y + i >= len(board) or board[y + i][x] != word[i]:
                        good = False
                        break
                if good:
                    ret += 1

        for y in range(len(board)):
            for x in range(len(board[0])):
                good = True
                for i in range(len(word)):
                    if y - i < 0 or board[y - i][x] != word[i]:
                        good = False
                        break
                if good:
                    ret += 1

        for y in range(len(board)):
            for x in range(len(board[0])):
                good = True
                for i in range(len(word)):
                    if x - i < 0 or y + i >= len(board) or board[y+i][x - i] != word[i]:
                        good = False
                        break
                if good:
                    ret += 1

        for y in range(len(board)):
            for x in range(len(board[0])):
                good = True
                for i in range(len(word)):
                    if x + i >= len(board[y]) or y + i >= len(board) or board[y+i][x + i] != word[i]:
                        good = False
                        break
                if good:
                    ret += 1

        for y in range(len(board)):
            for x in range(len(board[0])):
                good = True
                for i in range(len(word)):
                    if x + i >= len(board[y]) or y - i < 0 or board[y-i][x + i] != word[i]:
                        good = False
                        break
                if good:
                    ret += 1

        for y in range(len(board)):
            for x in range(len(board[0])):
                good = True
                for i in range(len(word)):
                    if x - i < 0 or y - i < 0 or board[y-i][x - i] != word[i]:
                        good = False
                        break
                if good:
                    ret += 1
                
        return ret
    
    def find_x(board):
        to_find = 'S S\n A \nM M'.split("\n")
        ret = 0
        cur = board
        for i in range(4):
            for y in range(len(cur)):
                for x in range(len(cur[0])):
                    bad = False
                    for dy in range(3):
                        for dx in range(3):
                            if not to_find[dy][dx].strip():
                                continue
                            if y + dy >= len(cur) or x + dx >= len(cur) or cur[y +dy][x+dx] != to_find[dy][dx]:
                                bad = True
                                break
                        if bad:
                            break
                    if not bad:
                        ret += 1
            cur = rotate90(cur)
        return ret

    if part2:
        return find_x(board)
    return normal_search(board)
    
result = main(real_input)
if result is not None:
    ans(result)
result = main(real_input, True)
if result is not None:
    ans(result)