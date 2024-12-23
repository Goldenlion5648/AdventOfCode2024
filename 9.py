from AoCLibrary import *
with open("input9.txt") as f:
    real_input = f.read()

def main(a: str, is_part2):
    if is_part2:
        return part2(a)
    return part1(a)


def part1(a : str):
    a = a.strip()
    ret = 0
    order = {}
    pos = 0
    id = 0
    last = 0
    while pos < len(a):
        if pos % 2 == 1:
            last += int(a[pos])
        else:
            for i in range(int(a[pos])):
                order[last] = (id)
                last += 1
            id += 1
        pos += 1
    last -= 1
    highest = last
    changed = True
    while changed:
        changed = False
        left = 0
        while left < last:
            done = False
            while last not in order:
                last -= 1
                if last < 0:
                    done = True
                    break
            if done:
                break
            while left in order:
                left += 1
                if left >= highest:
                    done = True
                    break
            if done:
                break
            if left >= last:
                break
            temp = order[last]
            order.pop(last)
            order[left] = temp
            changed = True
        left = 0
        last = highest
    
    for i in range(highest + 1):
        if i not in order:
            continue
        ret += i * order[i]
    return ret
    

def part2(a : str):
    a = a.strip()
    ret = 0
    order = {}
    pos = 0
    id = 0
    last = 0
    order2 = {}
    gaps = {}
    pos_overall = 0
    id_to_pos = {}
    while pos < len(a):
        num = int(a[pos])
        if pos % 2 == 1:
            last += num
            gaps[pos_overall] = num
            pos_overall += num
        else:
            for i in range(num):
                order[last] = id
                last += 1
            order2[pos_overall] = (id, num)
            id_to_pos[id] = pos_overall
            pos_overall += num
            id += 1
        pos += 1
    current_id = id - 1
    while current_id >= 0:
        file_position = id_to_pos[current_id]
        (id2, file_size) = order2[file_position]
        for gap_pos, gap_size in sorted(gaps.items()):
            if gap_pos > file_position:
                break
            if file_size > 0 and file_size <= gap_size:
                gaps.pop(gap_pos)
                gaps[file_position] = file_size
                order2.pop(file_position)
                order2[gap_pos] = (id2, file_size)
                break
        if file_size < gap_size:
            gaps[gap_pos + file_size] = gap_size - file_size
        current_id -= 1
    to_iter = sorted(order2.items())
    pos = 0
    for start, (id, file_size) in to_iter:
        pos = start
        for x in range(file_size):
            ret += id * pos
            pos += 1
    return ret




samp = r"""
2333133121414131402

""".lstrip("\n")

ans(main(real_input, False))
ans(main(real_input, True))