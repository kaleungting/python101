from functools import reduce
#reduce(function, data)
my_list = [1,2,3]

def accumulator(acc, item):
    return acc + item #it returns what your next input is going to be


print(reduce(accumulator ,my_list, 0))
print(reduce(lambda acc, x: acc + x, my_list, 0))
#acc = what you start with

#first acc = 0
# 0(acc) + 1(item)
#second acc = 1
# 1(acc) + 2(item)
#third acc = 3
# 3(acc) + 3(item)
# return 6
