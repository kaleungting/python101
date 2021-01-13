
#ITERATIVE USING STACK
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        stack = [root]

        while len(stack):
            curr = stack.pop()
            temp = curr.left
            curr.left = curr.right
            curr.right = temp

            if curr.left:
                stack.append(curr.left)

            if curr.right:
                stack.append(curr.right)

        return root

#RECURSIVE
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        right = self.invertTree(root.right)
        left = self.invertTree(root.left)

        root.right = left
        root.left = right