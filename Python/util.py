import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("calc_square took " + str((end - start) * 1000))
        return result

    return wrapper
