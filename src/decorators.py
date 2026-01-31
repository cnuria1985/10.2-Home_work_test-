
from functools import wraps


def log(filename=None):
     def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="UTF-8") as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok\n")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="UTF-8") as file:
                        file.write(f'{func.__name__} error: {e}. Inputs: {args} {kwargs}\n')
                else:
                    print(f'{func.__name__} error: {e}. Inputs: {args} {kwargs}')

        return wrapper
     return decorator


@log()
def my_function(x, y):
    return x + y


my_function('1', 2)
