import random
from roll_the_dice import choice
from roll_the_dice import eight_ball
from roll_the_dice import dice

def meta(ctx, cmdline):
    random.seed()
    return _meta(ctx, cmdline)

def _meta(ctx, cmdline):
    args = cmdline.split(':')
    command = args[0]
    action = ctx.new_action()

    if command == 'choice':
        choices = args[1:]
        if len(choices) < 2:
            raise ValueError('you must provide at least 2 choices')
        action.text = choice(choices)
    elif command == 'coin':
        action.text = choice(['heads', 'tails'])
    elif command == '8ball':
        action.text = eight_ball()
    elif command == 'range':
        low, high = args[1:]
        low = int(low)
        high = int(high)
        action.text = str(random.randrange(low, high))
    elif command.startswith('d'):
        die_size = int(command[1:])
        action.text = dice(die_size)
    else:
        raise ValueError('a valid roll option was not provided')

    return action
