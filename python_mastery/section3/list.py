basket = [1, 2, 3, 4, 5]

# print(len(basket))

# adding
# modifies list in place
# basket.append(100) #inserts at last element
# basket.insert(4,100) #inserts at index
# basket.extend([100, 101]) #appends list to the original list

# removing
# basket.pop()  # removes from end
# basket.pop()  # removes from whatever index, returns Popped element
# basket.remove(4) #removes from whatever index, returns None
# basket.clear() #empties list
print(basket)


# basket.index("a") #returns the index of where the letter could found
# ("a" in basket) #returns boolean True/False if the item is in the list
# basket.count("a") #returns number of occurrences in the list
# basket.sort() #modifies the list
# sorted(basket) #returns a new list
# basket.reverse()
# basket[::-1] #reverses a new list
# list(range(1,100)) #returns a list from 1-100

# " ".join(["hi","my","name","is","ken"]) #hi my name is ken

#list unpacking
a, b, c, *other, d = [1,2,3,4,5,6,7,8,9]
print(a) #1
print(b) #2
print(c) #3
print(other) # [4,5,6,7,8]
print(d) #9
