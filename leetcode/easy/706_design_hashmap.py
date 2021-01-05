class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = []

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        found = False
        for i, kv in enumerate(self.buckets):
            if kv[0] == key:
                self.buckets[i] = (key, value)
                found = True
                break
        if not found:
            self.buckets.append((key, value))
        print(self.buckets)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        for (k, v) in self.buckets:
            if k == key:
                return v

        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        for i, kv in enumerate(self.buckets):
            if key == kv[0]:
                del self.buckets[i]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

"""
use buckets to store values

key into the buckets

  1 N N N
_ _ _ _ _
0 1 2 3 4

[]


10

everytime you insert a number, you check to see if the list[n] exists, if it doesn't, keep appending None into list until you reach the index
"""
