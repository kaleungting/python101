class Solution:
    def firstUniqChar(self, s: str) -> int:
        tracker = collections.Counter(s)

        for i, el in enumerate(s):
            if tracker[el] == 1:
                return i

        return -1
