#map(func, iterable)
#does not modify original list, returns a new one

my_list = [1,2,3]
def multiply_by2(item):
    return item*2

print(list(map(multiply_by2, my_list))) #[2,4,6]
print(list(map(lambda x: x*2, my_list)))
print(my_list) #[1,2,3]

