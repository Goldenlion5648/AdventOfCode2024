from AoCLibrary import *
with open("input19.txt") as f:
    real_input = f.read()

def main(a : str, is_part2=False):
    a = a.strip()
    inp = AdventInput(data=a)
    options, to_make = inp.para
    options = set(options.split(", "))
    to_make = lines(to_make)
    
    @cache
    def dfs(remaining : str):
        if not remaining:
            return 1
        total = 0
        for word in options:
            if remaining.startswith(word):
                total += dfs(remaining.removeprefix(word))
        return total

    ways_to_make = dd(int)
    for word in to_make:
        ways_to_make[word] = dfs(word)

    def count_makeable1():
        return sum(bool(ways_to_make[x]) for x in to_make)
    
    def count_ways_to_make():
        return sum(ways_to_make.values())
    
    if is_part2:
        return count_ways_to_make()
    return count_makeable1()



ans(main(real_input))
ans(main(real_input, True))