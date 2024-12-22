from AoCLibrary import *
with open("input22.txt") as f:
    real_input = f.read()

def main(a : str, is_part2):
    a = a.strip()
    def mix(x, y):
        return x ^ y
    def prune(x):
        return x % 16777216
    def get_ones_digit(x):
        return x % 10
    def secret_maker(start):
        secret = start
        # mix
        while True:
            secret = mix(secret, secret * 64)
            # prune
            secret = prune(secret)
            divided = secret // 32
            secret = mix(secret, divided)
            secret = prune(secret)
            multiplied = secret * 2048
            secret = mix(secret, multiplied)
            secret = prune(secret)
            yield secret

    def get_price_changes(prices):
        changes = []
        for i in range(len(prices) - 1):
            changes.append(
                get_ones_digit(prices[i + 1]) - 
                get_ones_digit(prices[i]))
        counts = Counter()
        for i, four_prices in enu(windowed(changes, 4)):
            if four_prices not in counts:
                counts[four_prices] = get_ones_digit(prices[i+4])
        return counts

    def part1():
        ret = 0
        for starting_num in nums(a):
            cur_gen = secret_maker(starting_num)
            for i in range(2000):
                value = next(cur_gen)
            ret += value
        return ret

    def part2():
        overall = Counter()
        for starting_num in nums(a):
            cur_gen = secret_maker(starting_num)
            prices = [next(cur_gen) for _ in range(2000)]
            prices.insert(0, starting_num)
            overall += get_price_changes(prices)
        return max(overall.values())
    
    if is_part2:
        return part2()
    return part1()


ans(main(real_input, False))
ans(main(real_input, True))