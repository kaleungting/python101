# Higher Order Function

# a function that accepts another function in its parameter

def greet(func):
    func()


# if a function that returns another function
def hello():
    def func():
        return 5
    return func()


# decorator is a function that enhances another function
def my_decorator(func):
    def wrap_func():
        print("**************")
        func()
        print("**************")
    return wrap_func


@my_decorator  # wraps the hi function with the decorator
def hi():
    print("hi!")


@my_decorator  # reuse the decorator to wrap bye function in
def bye():
    print("bye!")

# this is basically what it's doing underneath the hood
# hello2 = my_decorator(hi)
# hello2()


hi()
bye()


# Decorator Pattern - makes decorator flexible because it can take in as many arguments and you dont have to worry
def my_decorator_pattern(func):
    def wrap_func(*args, **kwargs):
        func(*args, **kwargs)
    return wrap_func


@my_decorator_pattern
def howdy(greeting, emoji=";)"):
    print(greeting, emoji)


howdy("howdyyyy")


