from AoCLibrary import *
with open("input14.txt") as f:
    real_input = f.read()

class Robot:
    def __init__(self, pos_x, pos_y, vel_x, vel_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = vel_x
        self.vel_y = vel_y
    
    def move(self, x_bounds, y_bounds):
        self.pos_x += self.vel_x
        self.pos_x %= x_bounds
        self.pos_y += self.vel_y
        self.pos_y %= y_bounds
    
    def __repr__(self):
        return f"{self.pos_x},{self.pos_y} V={self.vel_x},{self.vel_y}"

    
def main(a : str, part2=True):
    a = a.strip()
    inp = AdventInput(data=a)
    ret = 0
    robots = []
    def show(robots, timestep):
        if timestep % 1000 == 0:
            debug(timestep)
        board = dd(lambda : ".")
        for robot in robots:
            board[robot.pos_y, robot.pos_x] = "#"
         
        show_board(board, show_anyway=True)
    
    def get_safety_factor():
        quad_counts = Counter()
        for robot in robots:
            x = None
            if robot.pos_x > x_dim // 2:
                x = 1
            elif robot.pos_x < x_dim // 2:
                x = 0

            y = None
            if robot.pos_y > y_dim // 2:
                y = 1
            elif robot.pos_y < y_dim // 2:
                y = 0
            if x is None or y is None:
                continue
            quad_counts[x, y] += 1
        return prod(quad_counts.values())


    for line in inp.lines:
        robots.append(Robot(*nums(line)))
    if len(robots) < 50:
        x_dim = 11
        y_dim = 7
    else:
        x_dim = 101
        y_dim = 103
    
    if not part2:
        for i in range(100):
            for robot in robots:
                robot.move(x_dim, y_dim)
        return get_safety_factor()
    else:
        for i in range(1, 100000):
            for robot in robots:
                robot.move(x_dim, y_dim)
            cur_positions = {(robot.pos_y, robot.pos_x) for robot in robots}
            done = False
            for pos in cur_positions:
                if all(element_wise_tup(pos, offset) in cur_positions for offset in adj8):
                    show(robots, i)
                    done = True
                    break
            if done:
                return i



ans(main(real_input, False))
ans(main(real_input, True))