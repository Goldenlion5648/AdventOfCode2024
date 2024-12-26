from AoCLibrary import *
with open("input24.txt") as f:
    real_input = f.read()

from z3 import Solver, Bool, sat, And, Xor, Or, is_true
import random

random.seed(345)
def main(a : str, is_part2=False):
    '''
    part 2 was solved with the below helpers, and looking at the graph
    using Graph Viz
    https://dreampuf.github.io/GraphvizOnline/
    '''
    a = a.strip()
    inp = AdventInput(data=a)
    starting_values, expressions = inp.para
    solver = Solver()
    name_to_var = {}
    all_x_y_variables = set()
    for line in starting_values.split("\n"):
        name, value = line.split(": ")
        value = bool(int(value))
        cur_var = Bool(name)
        name_to_var[name] = cur_var
        all_x_y_variables.add(cur_var)
        if not is_part2:
            solver.add(cur_var == value)
        
    
    result_to_input_names = dd(set)
    result_to_equation = {}
    
    def sum_bits_starting_with(letter, solved_values):
        cur_names = [name for name in name_to_var if name.startswith(letter)]
        cur_names.sort(reverse=True)
        res = 0
        for name in cur_names:
            if is_true(solved_values[name_to_var[name]]):
                res |= 1
            res <<= 1
        res >>= 1
        return res

    def get_bad_positions_helper(solver):
        if solver.check() != sat:
            assert False
        solved_values = solver.model()
        x_total = sum_bits_starting_with("x", solved_values)
        y_total = sum_bits_starting_with("y", solved_values)
        z_total = sum_bits_starting_with("z", solved_values)
        x_aligned = (bin(x_total)[2:].rjust(50, "0"))
        y_aligned = (bin(y_total)[2:].rjust(50, "0"))
        z_aligned = (bin(z_total)[2:].rjust(50, "0"))
        print(x_aligned)
        print(y_aligned)
        print(z_aligned)
        expected = x_total + y_total
        expected_aligned = (bin(expected)[2:].rjust(50, "0"))
        pos = 1
        bad_positions = []
        for offset in range(len(x_aligned)-1, -1, -1):
            if z_aligned[-(offset + 1)] != expected_aligned[-(offset + 1)]:
                bad_positions.append(offset)
            pos <<= 1
        bad_positions.reverse()
        print(bad_positions)
        return bad_positions

    all_expressions = []
    def read_input():
        for line in expressions.splitlines():
            v1_name, op, v2_name, _, result = line.split(" ")
            if v1_name not in name_to_var:
                name_to_var[v1_name] = Bool(v1_name)
            if v2_name not in name_to_var:
                name_to_var[v2_name] = Bool(v2_name)
            if result not in name_to_var:
                name_to_var[result] = Bool(result)
            if op == "XOR":
                op = Xor
            elif op == "AND":
                op = And
            else:
                op = Or
            
            all_expressions.append([v1_name, op, v2_name, result])
            result_to_input_names[result].add(v1_name)
            result_to_input_names[result].add(v2_name)
            result_to_equation[result] = all_expressions[-1]
    
    def part1():
        for (v1_name, op, v2_name, result) in result_to_equation.values():
            solver.add(op(name_to_var[v1_name], name_to_var[v2_name]) == name_to_var[result])
        if solver.check() == sat:
            solved_values = solver.model()
            z_names = [name for name in name_to_var if name.startswith("z")]
            z_names.sort(reverse=True)
            res = 0
            for name in z_names:
                if name.startswith("z"):
                    if is_true(solved_values[name_to_var[name]]):
                        res |= 1
                    res <<= 1
            res >>= 1
            return (res)
        assert False
        
        
    def part2_helper():
        running_bad_positions = Counter()
        for i in range(30):
            solver = Solver()
            for cur_var in all_x_y_variables:
                solver.add(cur_var == bool(random.randint(0, 1)))
            for (v1_name, op, v2_name, result) in result_to_equation.values():
                solver.add(op(name_to_var[v1_name], name_to_var[v2_name]) == name_to_var[result])
            cur_bad_positions = set(get_bad_positions_helper(solver))
            running_bad_positions += Counter(cur_bad_positions)
        print(running_bad_positions)
        print(sorted(running_bad_positions.keys()))

    read_input()
    return part1()



ans(main(real_input))