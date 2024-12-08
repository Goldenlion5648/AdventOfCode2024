from AoCLibrary import *
with open("input8.txt") as f:
    real_input = f.read()

def main(a : str, part2=False):
    a = a.strip()
    inp = AdventInput(data=a)
    board = inp.board 
    letter_positions = dd(set)
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] != '.':
                letter_positions[board[y][x]].add((y, x))
                
    hash_positions = set()
    for letter in letter_positions:
        for (p1, p2) in it.product(letter_positions[letter], repeat=2):
            if p1 == p2:
                continue
            (y1, x1), (y2, x2) = p1, p2
            y_off, x_off = (y2-y1), (x2-x1)
            allowed_offset = range(0, len(board) + 2) if part2 else [1]
            for dist in allowed_offset:
                hash_pos = (y2 + y_off*dist, x2 + x_off*dist)
                if hash_pos[0] in range(len(board)) and hash_pos[1] in range(len(board[0])):
                    hash_positions.add(hash_pos)
                else:
                    break
    return len(hash_positions)




result = main(real_input)
if result is not None:
    ans(result)

result = main(real_input, True)
if result is not None:
    ans(result)