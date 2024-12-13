from AoCLibrary import *
with open("input13.txt") as f:
    real_input = f.read()
from z3 import Int, Solver, sat

def main(a : str, part2):
    a = a.strip()
    inp = AdventInput(data=a)
    ret = 0
    def solve_equations(goal, options, part2=False):
        if part2:
            goal = [x + 10000000000000 for x in goal]
        goal_x, goal_y = goal
        change_x1, change_y1 = options[0]
        change_x2, change_y2 = options[1]
        solver = Solver()
        goal_xZ = Int('goal_x')
        goal_yZ = Int('goal_y')
        change_x1Z = Int('change_x1')
        change_x2Z = Int('change_x2')
        change_y1Z = Int('change_y1')
        change_y2Z = Int('change_y2')
        aZ = Int('a')
        bZ = Int('b')
        solver.add(goal_xZ == goal_x)
        solver.add(goal_yZ == goal_y)

        solver.add(change_x1Z == change_x1)
        solver.add(change_x2Z == change_x2)
        solver.add(change_y1Z == change_y1)
        solver.add(change_y2Z == change_y2)

        solver.add(goal_xZ == change_x1Z*aZ + change_x2Z*bZ)
        solver.add(aZ >= 0)
        solver.add(bZ >= 0)
        solver.add(goal_yZ == change_y1Z*aZ + change_y2Z*bZ)
        if solver.check() == sat:
            res = solver.model()
            return res[aZ].as_long() * 3 + res[bZ].as_long()
        else:
            return 0

            
    for section in inp.paragraphs:
        options = []
        for i, line in enu(lines(section)):
            if i < 2:
                options.append(tuple(nums(line)))
            else:
                goal = tuple(nums(line))
        ret += solve_equations(goal, options, part2)
    return ret

ans(main(real_input, False))
ans(main(real_input, True))