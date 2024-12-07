from AoCLibrary import *
with open("input7.txt") as f:
    real_input = f.read()

def concat(a, b):
    return int(str(a) + str(b))

def main(a : str, part2=False):
    a = a.strip()
    inp = AdventInput(data=a)
    ret = 0
    for line in inp.lines:
        expected_answer, *rest = nums(line)
        def dfs(remaining_nums):
            if len(remaining_nums) == 1:
                if remaining_nums[0] == expected_answer:
                    return remaining_nums[0]
                return 0
            if remaining_nums[0] > expected_answer:
                return 0
                
            options = [op.add, op.mul]
            if part2:
                options.append(concat)
            for option in options:
                found_answer = dfs([option(remaining_nums[0],remaining_nums[1])] +remaining_nums[2:])
                if found_answer != 0:
                    return  found_answer
            return 0
            
        ret += dfs(rest)
    return ret

result = main(real_input)
if result is not None:
    ans(result)
result = main(real_input, True)
if result is not None:
    ans(result)