from AoCLibrary import *
with open("input25.txt") as f:
    real_input = f.read()

def main(a : str):
    a = a.strip()
    inp = AdventInput(data=a)
    ret = 0
    def count_pins(group):
        group = transpose(group.split("\n"))
        counts = [x.count("#") - 1 for x in group]
        return counts
    keys = []
    locks = []
    for group in inp.para:
        top = group.splitlines()[0]
        if all(x == '#' for x in top):
            locks.append(count_pins(group))
        else:
            keys.append(count_pins(group))

    for key in keys:
        for lock in locks:
            combined = element_wise(key, lock)
            if all(x < 6 for x in combined):
                ret += 1
    return ret


ans(main(real_input))