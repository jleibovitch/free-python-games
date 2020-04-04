"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
from random import randrange
from typing import List
from freegames import square, vector

started = False
food = vector(0, 0)
snake: List[vector] = [vector(10, 0)]
aim = vector(0, -10)

def change(x: int, y: int):
    "Change snake direction."
    aim.x = x
    aim.y = y
    keyPress()

def keyPress():
    "Starts moving the snake in response to a key press, only if the game hasn't already started"
    # pylint: disable=global-statement
    global started
    if started is False:
        move()
    started = True

def inside(head: vector) -> bool:
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

setup(420, 420, 0, 0)
hideturtle()
tracer(False)
listen()
onkeypress(lambda: change(10, 0), 'Right')
onkeypress(lambda: change(-10, 0), 'Left')
onkeypress(lambda: change(0, 10), 'Up')
onkeypress(lambda: change(0, -10), 'Down')
onkeypress(keyPress)
done()
