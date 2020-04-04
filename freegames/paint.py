"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.

"""

from turtle import *
from freegames import vector

def line(start: vector, end: vector):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start: vector, end: vector):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circle(start: vector, end: vector):
    "Draw circle from start to end."
    pass  # TODO

def rectangle(start: vector, end: vector):
    "Draw rectangle from start to end."
    pass  # TODO

def triangle(start: vector, end: vector):
    "Draw triangle from start to end."
    pass  # TODO

def tap(x: float, y: float):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkeypress(undo, 'u')
onkeypress(lambda: color('black'), 'K')
onkeypress(lambda: color('white'), 'W')
onkeypress(lambda: color('green'), 'G')
onkeypress(lambda: color('blue'), 'B')
onkeypress(lambda: color('red'), 'R')
onkeypress(lambda: store('shape', line), 'l')
onkeypress(lambda: store('shape', square), 's')
onkeypress(lambda: store('shape', circle), 'c')
onkeypress(lambda: store('shape', rectangle), 'r')
onkeypress(lambda: store('shape', triangle), 't')
done()
