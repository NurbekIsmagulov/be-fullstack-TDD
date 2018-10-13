

def get_min(a, b):
    return a if a < b else b


def get_min_without_arguments():
    raise TypeError("Can not get min without arguments.")


def get_min_with_one_argument(x):
    return x


def get_min_with_many_arguments(*args):
    return min(args)


def get_min_with_one_or_more_arguments(first, *args):
    """
    min_number = first
    for arg in args:
        if arg < first:
            min_number = arg
    return min_number
    """
    return min(first, min(args))

def get_min_bounded(*args, low, high):
    min_number = float('inf')
    for arg in args:
        if arg < min_number and low < arg < high:
            min_number = arg
    return min_number


def make_min(*, low, high):
    def inner(first, *args):
        min_number = float('inf')
        for arg in (first, ) + args:
            if arg < min_number and low < arg < high:
                min_number = arg
        return min_number

    return inner
