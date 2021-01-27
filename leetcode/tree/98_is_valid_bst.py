class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validTree(root, float("-inf"), float("inf"))

    def validTree(self, node, lb, ub):
        if not node:
            return True

        if (node.val <= lb) or (node.val >= ub):
            return False

        return self.validTree(node.left, lb, node.val) and self.validTree(node.right, node.val, ub)
