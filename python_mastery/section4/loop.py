# for loops allow us to iterate through any ITERABLE item

#string, list, dictionary, sets, tuples,

# IMPORTANT - the LAST iterated value inside a loop can be printed outside of the loop itself

for ele in (1, 2, 3):
    print(ele)

# even though 'ele' is outside of the loop, it can still be accessed
print(f'hello my name is {ele}')

# looping through dictionary
player = {
    "name": "Ken",
    "team": "Boston Celtics",
    "class": "Point Guard",
    "jersey_number": 15
}

for key, value in player.items():
    print((key, value))

for item in player.keys():
    print(item)

for item in player.values():
    print(item)


# exercise

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum = 0
for num in my_list:
    sum += num
print(sum)


# range()
for _ in range(0, 10):
    print("do this 10 times")

# descending order
for _ in range(10, 0, -1):
    print(_)

# enumerate();

for i, ele in enumerate([1, 2, 3]):
    print(i, ele)


# break, continue, pass
# break - jump out of loop
# continue - move to the next iteration
# pass - placeholders

# picture = [
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0],
#     [1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0],
# ]

# for row in picture:
#     for ele in row:
#         if (ele == 0):
#             print(" ", end="")
#         else:
#             print("*", end="")
#     print("")


some_list = ["a", "b", "c", "d", "d", "b"]

newset = set()
newlist = []
for ele in some_list:
    if ele in newset:
        newlist.append(ele)
    newset.add(ele)

print(newlist)
