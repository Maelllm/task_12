from functools import reduce


def reduce_1(func, iterable, init=None):
    """Return result with used function (func) with all arguments from
    iterable object from left to right"""
    try:  # Exclude non-iterable object
        iterrator = iter(iterable)
    except:
        return 'Enter iterable object'
    if init is None:  # Set starting object for function
        value = next(iterrator)
    else:
        value = init  # Or use what was set in reduce argument init Warning! This argument will be used alongside
        # iterable object
    for i in iterrator:  # Making result with all objects in iterable
        value = func(value, i)
    return value


def test_reduce(*args):  # Try to check if our reduce_1 return proper value as original reduce
    try:
        assert reduce_1(*args) == reduce(*args), 'Try better reduce_1'
        return True
    except AssertionError as k:
        print(f'Error {k}')


def test_reduce_2(func, value=None): # Try to check if our reduce_1 return expected value
    try:
        assert func == value, 'Try better reduce_1'
        return 'Test complete'
    except AssertionError as h:
        print(f'Error {f}')


print(test_reduce(lambda x, y: x + y, [1, 2]))

print(test_reduce_2(reduce_1(lambda x, y: x + y, [1, 2]), value=3))
