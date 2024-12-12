from AoCLibrary import *
with open("input12.txt") as f:
    real_input = f.read()

def main(a : str, part2):
    a = a.strip()
    inp = AdventInput(data=a)
    ret = 0
    board = inp.board
    board_dict = read_grid(a, True)
    y_dim = len(board)
    x_dim = len(board[0])
    letter_to_spots = dd(set)
    for y in range(y_dim):
        for x in range(x_dim):
            letter_to_spots[board[y][x]].add((y, x))

    all_spots_seen = set()
    def bfs(start_y, start_x, part2=True):
        fringe = deque([(start_y, start_x)])
        cur_letter = board_dict[start_y, start_x]
        seen_len_before = len(all_spots_seen)
        letter_to_perimeters = dd(set)
        while fringe:
            cur = fringe.popleft()
            if cur not in board_dict or board_dict[cur] != cur_letter:
                continue
            if cur in all_spots_seen:
                continue
            all_spots_seen.add(cur)
            for offset in adj:
                new = element_wise_tup(cur, offset)
                if new not in letter_to_spots[cur_letter]:
                    letter_to_perimeters[cur_letter].add((cur, offset))
                fringe.append(new)
        
        if not part2:
            return len(letter_to_perimeters[cur_letter]) * (len(all_spots_seen) - seen_len_before)

        side_count = 0
        for perim_spot in letter_to_perimeters[cur_letter]:
            position, perim_offset = perim_spot
            touching_count = 0
            for offset in adj:
                potential = (element_wise_tup(position, offset), perim_offset)
                if potential in letter_to_perimeters[cur_letter]:
                    touching_count += 1
            if touching_count == 0:
                side_count += 1
            if touching_count == 1:
                #only count this as a side if the top or right is missing
                if all(
                    (element_wise_tup(position, offset), perim_offset) not in 
                    letter_to_perimeters[cur_letter]
                            for offset in [directions[0], directions[1]]
                    ):
                        side_count += 1

        return side_count * (len(all_spots_seen) - seen_len_before)
        
    for y in range(y_dim):
        for x in range(x_dim):
            ret += bfs(y, x, part2)
    return ret
    

ans(main(real_input, False))
ans(main(real_input, True))