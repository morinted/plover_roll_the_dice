from roll_the_dice.roll import _meta
import random

def test_range():
    """
    Ensure range limits are inclusive.
    """
    random.seed('range')
    results = [_meta('range:1:10') for x in range(0, 25)]
    results.sort(key=int)
    assert results[0] == '1'
    assert results[-1] == '10'

def test_coin():
    """
    Verify heads or tails can appear
    """
    random.seed('coin')
    (heads, tails) = [_meta('coin') for x in range(0, 2)]
    assert heads == 'heads'
    assert tails == 'tails'

def test_dice():
    """
    Verify dice
    """
    random.seed('dice')
    results = [_meta('d6') for x in range(0, 10)]
    results.sort()
    assert results[0] == '1'
    assert results[-1] == '6'

    results = [_meta('d10') for x in range(0, 10)]
    results.sort(key=int)
    assert results[0] == '0'
    assert results[-1] == '9'

    results = [_meta('d20') for x in range(0, 20)]
    results.sort(key=int)
    assert results[0] == '1'
    assert results[-1] == '20'

def test_choice():
    """
    Verify all choices are eligible.
    """
    random.seed('choice')
    results = [int(_meta('choice:1:2:3:4:5:6:7:8:9:10')) for x in range(0, 27)]
    results.sort()
    assert set(results) == set(range(1, 11))
