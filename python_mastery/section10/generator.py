# generators are iterables
# but not all iterables are generators


# range(100)
# list(range(100))


def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b


for x in fib(21):
    print(x)
