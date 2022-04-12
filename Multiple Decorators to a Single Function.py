def my_decorator(func):
    def wrapper():
        print("Step - 1")
        func()
        print("Step - 3")

    return wrapper


def repeat(func):
    def wrapper():
        func()
        func()
        func()

    return wrapper


@my_decorator
@repeat
def start_steps():
    print("Step - 2")


start_steps()