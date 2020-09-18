# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if (not p and not q):
            return True
        elif (p and q and p.val == q.val):
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False

s = Solution()
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
q = TreeNode(1)
q.right = TreeNode(2)
q.left = TreeNode(3)
res = s.isSameTree(p, q)
print(res)

        