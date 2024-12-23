from AoCLibrary import *
with open("input23.txt") as f:
    real_input = f.read()

def main(a : str, is_part2):
    a = a.strip()
    inp = AdventInput(data=a)
    G = dd(set)

    for line in inp.lines:
        x, y = line.split("-")
        G[x].add(y)
        G[y].add(x)


    if not is_part2:
        seen = set()
        for comp in G:
            for comp2 in G[comp]:
                third = G[comp] & G[comp2]
                for comp3 in third:
                    seen.add(t_sorted((comp, comp2, comp3)))
        with_t = sum(
            any(c.startswith("t") for c in group)
            for group in seen
        )
        return with_t

    times_seen = Counter()
    for comp in G:
        cur_group = G[comp] | {comp}
        for comp2 in G[comp]:
            cur_and = tsorted((G[comp2] | {comp2}) & cur_group)
            times_seen[cur_and] += 1
    return ",".join(max(times_seen, key=lambda x: times_seen[x]))



ans(main(real_input, False))
ans(main(real_input, True))