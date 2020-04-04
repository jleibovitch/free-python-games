import random
import runpy
import sys

import mockturtle

sys.modules['turtle'] = sys.modules['mockturtle']


def test_snake():
    random.seed(0)
    mockturtle.events[:] = (
        [('timer',), ('key Left',), ('timer',), ('key Up',), ('key Down',)]
        + [('timer', True)] * 300
    )
    runpy.run_module('freegames.snake')
    

if __name__ == "__main__":
    test_snake()