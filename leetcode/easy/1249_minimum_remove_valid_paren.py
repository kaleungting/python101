class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        delete = set()

        for i, char in enumerate(s):
            if char == ")":
                if len(stack) > 0:
                    stack.pop()
                else:
                    delete.add(i)
            elif char == "(":
                stack.append(i)

        for open_paren in stack:
            delete.add(open_paren)

        new_str = ""

        for i, char in enumerate(s):
            if i not in delete:
                new_str += char

        return new_str
