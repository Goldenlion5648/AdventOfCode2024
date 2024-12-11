from AoCLibrary import *
with open("input11.txt") as f:
    real_input = f.read()

def main(a : str, times_to_run):
    a = a.strip()
    a = nums(a)

    @cache
    def get_total_after_x(cur, cur_depth, goal_depth):
        if cur_depth == goal_depth:
            return 1
        if cur == 0:
            cur = 1
        elif len(str(cur)) % 2 == 0:
            as_str = str(cur)
            left_digits, right_digits = lmap(int, [as_str[:len(as_str)//2], as_str[len(as_str)//2:]])
            left_total = get_total_after_x(left_digits, cur_depth + 1, goal_depth)
            right_total = get_total_after_x(right_digits, cur_depth + 1, goal_depth)
            return left_total + right_total
        else:
            cur *= 2024
        return get_total_after_x(cur, cur_depth + 1, goal_depth)

    return sum(get_total_after_x(x, 0, times_to_run) for x in a)


ans(main(real_input, 25))
ans(main(real_input, 75))