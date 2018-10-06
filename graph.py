import time
from line import Line

axiomatic_line = Line([0, -200], [0, 200])

queue = [axiomatic_line]

while True:
    line = queue.pop(0)
    line.draw()
    queue.extend(line.get_children())
