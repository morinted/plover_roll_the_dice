import random

def dice(sides):
    if sides == 10:
        # Of course d10s have to be different.
        return str(random.randrange(0, 9))
    else:
        return str(random.randrange(1, sides))