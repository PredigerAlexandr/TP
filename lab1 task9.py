import functools

def cache(func):
    @functools.wraps(func)
    def new_func(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        print(cache_key)
        if cache_key not in new_func.cache:
            new_func.cache[cache_key] = func(*args, **kwargs)
        return new_func.cache[cache_key]
    new_func.cache = dict()
    return new_func

@cache
def fib(num):
    if num < 2:
        return num
    return fib(num - 1) + fib(num - 2)
print(fib(10))