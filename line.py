import math
import turtle

pen = turtle.Turtle()
pen.ht()
pen.speed(5000)
pen.pencolor('black')

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self):
        pen.up()
        pen.goto(self.start[0], self.start[1])
        pen.down()
        pen.goto(self.end[0], self.end[1])

    def print_data(self):
        print(f'Line: ({self.start}, {self.end})')

    def get_children(self):
        # NOTE: This functions sometimes returns invisible children.

        diff_x = self.start[0] - self.end[0]
        diff_y = self.start[1] - self.end[1]
        length = math.sqrt(pow(diff_x, 2) + pow(diff_y, 2))
        midpoint = [self.start[0] - diff_x / 2, self.start[1] - diff_y / 2]
        is_horizontal = True if diff_x == 0 else False

        child_1 = Line(self.start, midpoint)
        child_2 = Line(midpoint, self.end)
        child_3 = None

        if not is_horizontal:
            start = [midpoint[0], midpoint[1] - length / 4]
            end = [midpoint[0], midpoint[1] + length / 4]
            child_3 = Line(start, end)
        else:
            start = [midpoint[0] - length / 4, midpoint[1]]
            end = [midpoint[0] + length / 4, midpoint[1]]
            child_3 = Line(start, end)

        return [child_1, child_2, child_3]
