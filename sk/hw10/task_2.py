def repeat_me(count=2):
    def decorator(func):
        def wrapper(*args):
            for i in range(count):
                func(*args)

        return wrapper
    return decorator


@repeat_me(3)
def example(text):
    print(text)


example("start")
