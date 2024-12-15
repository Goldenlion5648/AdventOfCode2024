from AoCLibrary import *
with open("input15.txt") as f:
    real_input = f.read()

def main(a : str, part2=True):
    a = a.strip()
    def show(y_dim, x_dim, boxes, walls, lefts=None, rights=None):
        if not ("d" in sys.argv or "debug" in sys.argv):
            return
        for y in range(y_dim):
            for x in range(x_dim):
                cur = y, x
                if lefts is not None and cur in lefts:
                    debug("[", end='')
                elif rights is not None and cur in rights:
                    debug("]", end='')  
                elif cur in boxes:
                    debug("O", end='')
                elif cur in walls:
                    debug("#", end='')
                else:
                    debug(".", end='')
            debug()
    
    def get_replacement(to_replace):
        if to_replace == "#":
            return "##"
        if to_replace == "O":
            return "[]"
        if to_replace == ".":
            return ".."
        if to_replace == "@":
            return "@."
        return to_replace
        
    def get_box_to_right_of(left):
        return element_wise_tup(left, directions[">"])

    def get_box_to_left_of(right):
        return element_wise_tup(right, directions["<"])

    boxes = set()
    top_section = a.split("\n\n")[0]
    if part2:
        top_section = ''.join(get_replacement(x) for x in top_section)
    board_array = read_grid(top_section, False)
    y_dim = len(board_array)
    x_dim = len(board_array[0])
    board = read_grid(top_section, True)
    cur = find_in_grid(top_section, "@")
    arrows = "".join(a.split("\n\n")[1].split("\n")).strip()
    walls = set()
    lefts = set()
    rights = set()
    for y in range(y_dim):
        for x in range(x_dim):
            if board[y, x] == "O":
                boxes.add((y, x))    
            if board[y, x] == "#":
                walls.add((y, x))
            if board[y, x] == "[":
                lefts.add((y, x))
            if board[y, x] == "]":
                rights.add((y, x))

    for arrow in arrows:
        offset = directions[arrow]
        new = element_wise_tup(cur, offset)
        to_push = set()
        if not part2:
            while new in boxes:
                to_push.add(new)
                new = element_wise_tup(new, offset)
            if new in walls:
                continue
            boxes -= to_push
            to_push = {element_wise_tup(pos, directions[arrow]) for pos in to_push}
            boxes |= to_push
        else:
            bad = False
            to_check = [new]
            seen = set()
            lefts_to_push = set()
            rights_to_push = set()
            while len(to_check):
                new = to_check.pop()
                if new in walls:
                    bad = True
                    break
                if new in seen:
                    continue 
                seen.add(new)
                if new in lefts:
                    to_check.append(get_box_to_right_of(new))
                    lefts_to_push.add(new)
                    new = element_wise_tup(new, offset)
                    to_check.append(new)
                    
                if new in rights:
                    to_check.append(get_box_to_left_of(new))
                    rights_to_push.add(new)
                    new = element_wise_tup(new, offset)
                    to_check.append(new)
                    
            if bad:
                continue

            lefts -= lefts_to_push
            lefts |= {element_wise_tup(pos, offset) for pos in lefts_to_push}

            rights -= rights_to_push
            rights |= {element_wise_tup(pos, offset) for pos in rights_to_push}
            
        cur = element_wise_tup(cur, offset)
    
    def get_score(boxes):
        return sum(y * 100 + x for (y, x) in boxes)
    

    if not part2:
        return get_score(boxes)
    return get_score(lefts)


ans(main(real_input, False))
ans(main(real_input, True))