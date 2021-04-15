import random
from roll_the_dice import choice
from roll_the_dice import eight_ball
from roll_the_dice import dice

def meta(ctx, cmdline):
    random.seed()
    action = ctx.new_action()
    action.text = _meta(cmdline)
    return action

def _meta(cmdline):
    command, *args = cmdline.split(':')
    if command == 'choice':
        # {:roll:choice:option 1:option 2:option n}
        choices = args
        if len(choices) < 2:
            raise ValueError('you must provide at least 2 choices')
        return choice(choices)
    if command == 'coin':
        # {:roll:coin}
        return choice(['heads', 'tails'])
    if command == '8ball':
        # {:roll:8ball}
        return eight_ball()
    if command == 'range':
        # {:roll:range:1:10}
        low, high = args
        low = int(low)
        high = int(high) + 1 # Add 1 as randrange is [low, high)
        return str(random.randrange(low, high))
    if command.startswith('d'):
        # {:roll:dN} where N is a positive integer.
        die_size = int(command[1:])
        return dice(die_size)

    raise ValueError('a valid roll option was not provided')
