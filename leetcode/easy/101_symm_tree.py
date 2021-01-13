class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)

    def isMirror(self, t1, t2):
        if t1 == None and t2 == None:
            return True
        if (t1 == None and t2 != None) or (t2 == None and t1 != None):
            return False
        return t1.val == t2.val and self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)


"""
using a helper function recursively check the left and the right to see if it's a mirror

if both reaches None, that means you've gone down the tree and it hasn't returned False yet, so return True
if one side has reached None but the other side is not None yet, then that means they are not symmetric

return boolean TRUE or False if
    t1.val == t2.val
    recursively call isMirror on t1.left, t2.right and vice versa t1.right, t2.left


"""