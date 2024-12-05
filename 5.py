from AoCLibrary import *
with open("input5.txt") as f:
    real_input = f.read()

def main(a : str, part2=False):
    a = a.strip()
    inp = AdventInput(data=a)
    ret = 0
    requirements_for = defaultdict(set)
    what_comes_after = defaultdict(set)
    x_and_y, orderings = inp.sections
    for line in x_and_y.splitlines():
        x, y = nums(line)
        requirements_for[y].add(x)
        what_comes_after[x].add(y)
    orderings = orderings.splitlines()
    def is_valid_ordering(some_order):
        not_allowed = set()
        for num in some_order:
            if num in not_allowed:
                return False
            not_allowed |= requirements_for[num]
        return True

    def get_correct_order_for(some_order):
        requirements_left = dd(set)
        all_here = set(some_order)
        for x in some_order:
            requirements_left[x] = requirements_for[x].copy()
            requirements_left[x] = {z for z in requirements_left[x] if z in all_here}
        new_order = []
        fringe = deque(some_order)
        debug("requirements_left", requirements_left)
        seen = set()
        while fringe:
            x = fringe.popleft()
            if x in seen:
                continue
            if len(requirements_left[x]) == 0:
                new_order.append(x)
                seen.add(x)
                for y in what_comes_after[x]:
                    if y in requirements_left:
                        requirements_left[y].discard(x)
                        if len(requirements_left[y]) == 0:
                            fringe.append(y)
            else:
                fringe.append(x)
        return new_order


    orderings = [nums(temp) for temp in orderings]
    debug(requirements_for)
    for cur in orderings:
        bad = not is_valid_ordering(cur)
        debug("bad", bad)
        if bad and part2:
            fixed = get_correct_order_for(cur)
            debug("fixed", fixed)
            ret += fixed[len(fixed)//2]

        if not bad:
            if not part2:
                ret += cur[len(cur)//2]
        
    return ret

result = main(real_input)
ans(result)
result = main(real_input, True)
ans(result)