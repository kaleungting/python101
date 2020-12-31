# Fundamental Data Types

int  # whole numbers

# math functions
round(3.9)
abs(-10)
bin(5) -> '0b101'
int('0b101', 2) -> 5

# floating point number, number with a decimal point (takes up more space in memory than an int, because of BINARY)
float
bool
str
list
tuple
set
dict

# Classes -> custom types

# Specialized Data Types

None


"""
Variables
    snake_case
    start with letter or underscore
    case sensitive
    can't overwrite keywords
"""


"""
Augmented assignment operator
    +=
    -=
    *=
    //=
    %=
"""

"""
Escape sequences
\" - quote
\n - new line
\t - tab
"""

"""
formatted string
(f'hi my {name}. I am {age} years old')


string indexes
[start:stop:stepover]
stepover defaults to 1
negative index, starts at end


"""

birth_year = input('what year were you born?')
age = 2019 - int(birth_year)
print(f'your age is {age}')


# Strings aren't mutable but lists are
# everytime you SLICE a list, it'll create a new object, but if you set a variable equal to an old variable, then it only creates a shallow copy

new_cart = amazon_cart #THIS WILL ONLY CREATE A SHALLOW COPY
new_cart = amazon_cart[:] #THIS IS HOW U MAKE A DEEP COPY
