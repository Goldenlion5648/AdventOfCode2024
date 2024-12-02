from AoCLibrary import *
with open("input2.txt") as f:
    real_input = f.read()

def main(a : str, part2=False):
    a = a.strip()
    inp = AdventInput(data=a)
    ret = 0
    for line in inp.lines:
        cur = nums(line)
        if not part2:
            ret += is_safe(cur)
            continue
        for y in range(len(cur)):
            temp = cur[:y] + cur[y + 1:]
            good = is_safe(temp)
            if good:
                ret += 1
                break
    return ret


def is_safe(cur):
    return (
        all([cur[i] < cur[i + 1] and abs(cur[i] - cur[i + 1]) in range(1, 4) 
                    for i in range(len(cur) - 1)]) 
            or
        all([cur[i] > cur[i + 1] and abs(cur[i] - cur[i + 1]) in range(1, 4) 
                    for i in range(len(cur) - 1)])
    )




samp = r"""
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9

""".lstrip("\n")

if samp and "r" not in sys.argv:
    sample_answer = main(samp)
    print("sample", sample_answer)
else:
    print("no sample provided")

if "s" in sys.argv:
    exit()
result = main(real_input)
if result is not None:
    ans(result)
result = main(real_input, True)
if result is not None:
    ans(result)