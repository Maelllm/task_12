def reduce(func, iterable, init=None):
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


print(reduce(lambda x, y: x * y, 3))
print(reduce(lambda x, y: x * y, [3, 4, 5]))
print(reduce(lambda x, y: x * y, [3, 4, 5], init=4))
