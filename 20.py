from AoCLibrary import *
with open("input20.txt") as f:
    real_input = f.read()

def main(a : str, is_part2=False):
    a = a.strip()
    start = find_in_grid(a, "S")
    end = find_in_grid(a, "E")
    board = dd(lambda : "#")
    board.update(read_grid(a, True))
    y_dim, x_dim = board_dims(board)
    distances = dd(lambda : inf)
    def show(used):
        if not is_debug():
            return
        for y in range(y_dim):
            for x in range(x_dim):
                if (y, x) in used:
                    debug("C", end='')
                else:
                    debug(board[y, x], end='')
            debug()
        input()
    def search(board, steps_that_must_be_saved):
        search_mode = steps_that_must_be_saved == 0
        fringe = deque([(start, 0, -1 if search_mode else 20, None, None)])
        goal = end
        while fringe:
            cur, steps, cheats_remaining, cheat_start, cheat_end = (fringe).popleft()
            id = cur
            if distances[id] < steps:
                continue
            distances[id] = steps

            if cur == goal:
                continue
            for offset in adj:
                new = element_wise_tup(cur, offset)
                if new[0] not in range(0, y_dim) or new[1] not in range(0, x_dim):
                    continue

                if board[new] != "#":
                    if search_mode:
                        fringe.append((new, steps + 1, cheats_remaining, cheat_start, cheat_end))

        return 10000000
    
    search(board, 0)
    
    def solve(cheat_steps):
        saved_counts2 = Counter()
        for p1, p2 in it.combinations(sorted(distances.keys()), 2):
            manhat_between = manhat(p1, p2)
            dist_saved = abs(distances[p1] - distances[p2]) - manhat_between
            if manhat_between <= cheat_steps and dist_saved >= 100:
                saved_counts2[dist_saved] += 1
        return sum(saved_counts2.values())
    
    if is_part2:
        return solve(20)
    return solve(2)


ans(main(real_input, False))
ans(main(real_input, True))