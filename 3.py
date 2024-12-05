from AoCLibrary import *
with open("input3.txt") as f:
    real_input = f.read()

def main(a : str, part2=False):
    a = a.strip()
    if not part2:
        parts = re.findall(r"mul\(\d+,\d+\)", a)
        return sum(prod(nums(p)) for p in parts)

    ret = 0
    is_good = True
    keeps = re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", a)
    for k in keeps:
        if k.startswith("don"):
            is_good = False
        elif k.startswith("do"):
            is_good = True
        else:
            if is_good:
                ret += prod(nums(k))
    return ret

result = main(real_input)
if result is not None:
    ans(result)

result = main(real_input, True)
if result is not None:
    ans(result)