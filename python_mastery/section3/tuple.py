# tuple

# immutable, can access through index but can't reassign or change
# makes code more predictable but less flexible
# they are usually a bit faster/performant

# tuple can be a key in a dictionary
my_tuple = (1, 2, 3, 4, 5)
new_tuple = my_tuple[1:2]

# returns (2,) tuples that return a single item has a comma in the end
print(new_tuple)

x, y, z, *other = (1, 2, 3, 4, 5, 6, 7)

print(other) #returns [4,5,6,7]

#tuple methods
#tuple.count(5)
#tuple.index(3) return 2