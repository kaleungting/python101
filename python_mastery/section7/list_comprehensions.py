# list comprehension,
# add a function to modify each iterable, option of adding a conditional at the end as well
#[function, iterable, conditional]

my_list = [char for char in "hello"]
my_list2 = [num*2 for num in range(0, 100)]
my_list3 = [num*2 for num in range(0, 100) if num % 2 == 0]


# print(my_list)
# print(my_list2)
# print(my_list3)

simple_dict = {
    'a': 1,
    'b': 2
}

my_dict = {key: value**2 for key, value in simple_dict.items() if value %
           2 == 0}

print(my_dict)

some_list = ['a','b','c','b','d','m','n','n']
duplicates = list(set([char for char in some_list if some_list.count(char) > 1]))
print(duplicates)