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
        randomize_food()
        move()
    started = True

def inside(head: vector) -> bool:
    "Return True if head inside boundaries."
    return -210 < head.x < 200 and -200 < head.y < 200

def vector_inside_snake(snake_head: vector):
    "Returns true if the given vector is inside of the snake"
    for snake_vector in snake:
        if snake_vector.x == vector.x and snake_vector.y == vector.y:
            return True
    return False

def randomize_food():
    "Randomizes the location of the food"
    while True:
        newVector = vector(randrange(-15, 15) * 10, randrange(-15, 15) * 10)
        if not vector_inside_snake(newVector):
            food.x = newVector.x
            food.y = newVector.y
            break

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
        randomize_food()
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
