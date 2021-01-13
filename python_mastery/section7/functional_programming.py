#Pure Function - it only affects the argument and doesn't touch anything on the outside world


# new_list = [] this HAS side effects
def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    #print(new_list) this HAS side effects
    return new_list 
    

print(multiply_by2([1,2,3]))
