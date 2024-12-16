from AoCLibrary import *
with open("input16.txt") as f:
    real_input = f.read()

def main(a : str):
    a = a.strip()
    start = find_in_grid(a, "S")
    goal = find_in_grid(a, "E")
    def search(known_goal_dist=inf):
        is_part2 = known_goal_dist != inf
        fringe = deque([(0, start, directions[1], {start})])
        seen = dd(lambda : inf)
        board = read_board(a, "S", "E", "#")[0]
        y_dim, x_dim = board_dims(board)
        def show(used):
            for y in range(y_dim):
                for x in range(x_dim):
                    if board[y, x]:
                        debug("#", end='')
                    elif (y, x) in used:
                        debug("O", end='')
                    else:
                        debug(".", end='')
                debug()
            input()

            
        for offset in adj4:
            seen[goal, offset] = known_goal_dist
        final_spots = set()
        
        while fringe:
            steps, cur, facing, used = fringe.popleft()
            cur_with_facing = (cur, facing)
            if steps > seen[goal]:
                continue
            if steps > seen[cur_with_facing]:
                continue
            if not is_part2 and steps == seen[cur_with_facing]:
                continue
            seen[cur_with_facing] = steps
            if cur == goal:
                seen[goal] = min(seen[goal], steps)
                final_spots |= used
                continue
            option_count = 0
            for offset in adj4:
                new = element_wise_tup(cur, offset)
                new_steps = steps + 1
                if offset != facing:
                    new_steps += 1000
                if new not in used and not board[new]:
                    new_state = (new_steps, new, offset, used | {new})
                    fringe.append(new_state)
                    option_count += 1
            
        if not is_part2:
            return seen[goal]
        return len(final_spots)

    dist = search()
    return dist, search(dist)

ans(main(real_input))