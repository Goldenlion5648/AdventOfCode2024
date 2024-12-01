from AoCLibrary import *
with open("input1.txt") as f:
    real_input = f.read()

def main(a : str, part2=False):
    a = a.strip()
    inp = AdventInput(data=a)
    left, right = transpose([nums(line) for line in inp.lines])
    left.sort()
    right.sort()
    if part2:
        counts = Counter(right)
        return sum(x * counts[x] for x in left)
    return sum(abs(left[i] - right[i]) for i in range(len(left)))
    

samp = r"""
3   4
4   3
2   5
1   3
3   9
3   3

""".lstrip("\n")

if samp and "r" not in sys.argv:
    sample_answer = main(samp)
    print("sample", sample_answer)
else:
    print("no sample provided")

if "s" in sys.argv:
    exit()
result = main(real_input)
ans(result)
result = main(real_input, True)
ans(result)