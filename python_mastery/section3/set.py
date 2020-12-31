# unordered, unique values, one location in memory

test_set = {1, 2, 3, 4, 5, 5}
my_list = [1, 2, 3, 4, 5, 5]
print(set(my_list))  # returns only unique value

# len(my_set) #return 6
# (1 in my_set) #return true
# my_set.copy()

my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

my_set.difference(your_set)  # {1,2,3}
my_set.discard(5)  # returns None, but will remove element from the set
# returns None, but my_set will become {1,2,3}. it removes the elements in common
my_set.difference_update(your_set)
# {4,5} returns what's in common
my_set.intersection(your_set) or (my_set & your_set)
# returns Boolean if there are any overlapping elements
my_set.isdisjoint(your_set)
# returns a combination of both sets
my_set.union(your_set) or (my_set | your_set)
my_set.issubset(your_set)  # returns boolean to see if set is a subset
my_set.issuperset(your_set)  # returns boolean to see if the set is a superset
