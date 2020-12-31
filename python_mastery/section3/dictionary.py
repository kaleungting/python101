# Dictionary
# dict - a way to organize data (Key/Value pair)

user = {
    "a": 1,
    "b": 2
}

user2 = dict(name="ken")  # different way of creating a dictionary
print(user["b"])

#tuple can be a key in a dictionary

#dictionary methods
#user["c"] #ERROR
#user.get("c") #return None
#user.get("c", 3) #if c doesn't exist, then set the value of 3 to c
#user.values()
#user.keys()
#user.items(), RETURNS k,v pair as TUPLES
#user.clear() empties a dictionary
#user.copy() makes a new copy
#user.pop("a") removes from dictionary and returns value
#user.popitem() removes RANDOM
#user.update({"a" : 100}) update key if there, adds key if it isn't
