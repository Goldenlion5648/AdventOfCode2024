from AoCLibrary import *
with open("input21.txt") as f:
    real_input = f.read()

class RobotType(Enum):
    NUMERIC = 1
    DIRECTIONAL = 2

EMPTY = "B"
CONFIRM_BUTTON = "A"
offset_direction_to_arrow = {
    (-1, 0) : "^",
    (1, 0) : "v",
    (0, -1) : "<",
    (0, 1) : ">",
}
arrow_to_offset = rev_dict(offset_direction_to_arrow)

arrow_complements = {
    "^": "v",
    "v": "^",
    "<": ">",
    ">": "<",
}

robot_type_to_keypad = {
    RobotType.DIRECTIONAL : [
        [EMPTY, "^", CONFIRM_BUTTON],
        ["<",   "v", ">"],
    ],
    RobotType.NUMERIC: [
        ["7",   "8", "9"],
        ["4",   "5", "6"],
        ["1",   "2", "3"],
        [EMPTY, "0", CONFIRM_BUTTON]
    ]
}

class Robot:
    def __init__(self):
        self.x = -10
        self.y = -10
        self.keypad = [[]]
        self.type = -1
        assert False

@cache
def get_paths_for_pair(start_y, start_x, to_find, robot_type):
    def get_score(steps):
        score = 0
        for i in range(len(steps) - 1):
            if steps[i] == steps[i + 1]:
                score += 1000000
        return 10000 - (len(steps)*1000) + score
    fringe = deque([(start_y, start_x, [])])
    best_len = inf
    all_options = []
    cur_keypad = robot_type_to_keypad[robot_type]
    while fringe:
        cur_y, cur_x, movements = fringe.popleft()
        if cur_keypad[cur_y][cur_x] == to_find:
            all_options.append(movements + [CONFIRM_BUTTON])
            best_len = min(best_len, len(movements))
            continue
        if len(movements) > best_len:
            continue
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_y = cur_y + dy
            new_x = cur_x + dx
            current_arrow = offset_direction_to_arrow[dy, dx]
            if (
                new_y in range(len(cur_keypad)) and 
                new_x in range(len(cur_keypad[0])) and
                cur_keypad[new_y][new_x] != EMPTY and
                (not movements or movements[-1] != arrow_complements[current_arrow])
            ):
                fringe.append((new_y, new_x, movements + [current_arrow]))
    highest_score = max(get_score(x) for x in all_options)
    all_options = [x for x in all_options if get_score(x) == highest_score]
    return all_options


@cache
def get_pos_in_grid(to_find, robot_type=RobotType.DIRECTIONAL):
    board = robot_type_to_keypad[robot_type]
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == to_find:
                return (y, x)
    assert False, to_find


def main(a : str, is_part2):
    a = a.strip()
    inp = AdventInput(data=a)
    ret = 0
    middle_size = 26 if is_part2 else 3
    @cache
    def dfs(depth, start_y, start_x, end_y, end_x, robot_type):
        if depth >= middle_size:
            return 1
        
        board = robot_type_to_keypad[robot_type]
        options = get_paths_for_pair(start_y, start_x, 
                        board[end_y][end_x], 
                        robot_type)
        lowest = inf
        for path in options:
            lowest = min(lowest, get_path_cost(path, depth))
        return lowest

    def get_path_cost(path, depth):
        first = None
        path_total = 0
        if len(path) == 1:
            return 1
        path = CONFIRM_BUTTON + "".join(path)
        robot_type = RobotType.NUMERIC if depth == -1 else RobotType.DIRECTIONAL
        for p1, p2 in it.pairwise(path):
            if first is None:
                first = p1
            path_total += dfs(depth + 1, 
                        *get_pos_in_grid(p1, robot_type),
                        *get_pos_in_grid(p2, robot_type),
                        robot_type)
        return path_total

    for line in inp.lines:
        size = get_path_cost(line, -1)
        number = num(line)
        ret += size * number
    return ret


ans(main(real_input, False))
ans(main(real_input, True))