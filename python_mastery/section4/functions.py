# function allows code to be DRY and reusable

def say_hello():
    # docstrings
    """
    Info: this function prints out hello
    """
    print('hello')


say_hello()

# interpretter goes line by line, so a function cant be invoked before it is defined
# parameters - name of variables that the function takes in (defined)
# arguments - actually value provided into the function (called/invoked)
# positional arguments - position matter
# keyword arguments - putting assignment as arguments

# METHODS VS FUNCTIONS

# methods have to be owned by something
# "hello".capitalize()
# dictionary.count("A")
# .clear(), .pop()


'''
ARGS and KEYWORD ARGS

*a **kwargs

'''


def super_func(*args, **kwargs):
    print(args)  # return as a tuple
    print(kwargs)  # return as a dictionary


super_func(1, 2, 3, 4, 5, num1=6, num2=7)

#RULE: params, *args, default params, **kwargs

def highest_even(li):
    return max(filter(lambda ele: ele % 2 == 0, li))

print(highest_even([1,2,3,4,5,100,7,8,9,10]))