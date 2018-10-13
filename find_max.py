def get_max(a, b):
    return a if a > b else b


def get_max_without_arguments():
    raise TypeError("Can not get max without arguments.")


def get_max_with_one_argument(a):
    return a


def get_max_with_many_arguments(*args):
    return max(args)


def get_max_with_one_or_more_arguments(first, *args):
    return max(first, max(args))


def get_max_bounded(*args, low, high):
    max_number = float('-inf')
    for arg in args:
        if arg > max_number and low < arg < high:
            max_number = arg
    return max_number

def make_max(*, low, high):
    def inner(first, *args):
        max_number = float('-inf')
        for arg in (first,) + args:
            if arg > max_number and low < arg < high:
                max_number = arg
        return max_number
    return inner
