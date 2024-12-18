from AoCLibrary import *
with open("input17.txt") as f:
    real_input = f.read()

def main(a : str, is_part2=False):
    a = a.strip()
    registers = dd(int)
    all_lines = lines(a)
    registers["A"] = num(all_lines[0])
    registers["B"] = num(all_lines[1])
    registers["C"] = num(all_lines[2])
    program = nums(all_lines[-1])
    def adv(register_to_store_in, pos):
        registers[register_to_store_in] = registers["A"] // (2 ** get_combo_operand(program[pos + 1]))
    def get_combo_operand(value):
        if 1 <= value <= 3:
            return value
        assert value != 7
        convert = {
            4 : "A",
            5 : "B",
            6 : "C",
        }
        return registers[convert[value]]


    def part1():
        output = []
        pos = 0
        while (pos >= 0 and pos < len(program)):
            if program[pos] == 0:
                adv("A", pos)
            elif program[pos] == 1:
                registers["B"] = registers["B"] ^ (program[pos + 1])
            elif program[pos] == 2:
                registers["B"] = get_combo_operand(program[pos + 1]) % 8
            elif program[pos] == 3:
                if registers["A"] == 0:
                    pos += 2
                    continue
                pos = program[pos + 1]
                continue
            elif program[pos] == 4:
                registers["B"] = registers["B"] ^ registers["C"]
            elif program[pos] == 5:
                output.append(get_combo_operand(program[pos + 1]) % 8)
            elif program[pos] == 6:
                adv("B", pos)
            elif program[pos] == 7:
                adv("C", pos)
            pos += 2
        return str_list(output, ",")
    
    if not is_part2:
        return part1()
    
    needed = program
    def solve_part2(start, pos_in_answer):
        A = start
        B = A % 8
        B ^= 2
        C = A // (2 ** B)
        A >>= 3
        B ^= C
        B ^= 7
        out = B % 8
        # print("c", C)
        if out != needed[pos_in_answer]:
            return -1
        if pos_in_answer == 0:
            return start
        for i in range(8):
            found = solve_part2(int(bin(start)[2:].rjust(3, "0") + bin(i)[2:].rjust(3, "0"), 2), pos_in_answer - 1)
            if found != -1:
                return found
        return -1

    for i in range(8):
        worked = solve_part2(i, len(needed) - 1)
        if worked != -1:
            return worked

ans(main(real_input))
ans(main(real_input, True))