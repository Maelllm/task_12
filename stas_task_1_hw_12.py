def genet_1(some_number: int):
    full_list = range(some_number)
    i = 0
    while len(full_list) > i:
        yield full_list[i]
        i += 1


def genet_2(some_text: str):
    for i in some_text:
        yield i


def genet_3(some_text: str):
    a = 0
    while len(some_text) > a:
        yield f' {some_text} index is {a}'
        a += 1


def genet_4():
    i = 0
    while True:
        yield i ** 2 - i * 2 + 4
