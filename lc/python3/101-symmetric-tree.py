# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# 
# [1, 2, 2, 3, 4, 4, 3]


class Solution:

    # def flatten(self, root: TreeNode, xs):
    #     print(xs)
    #     if (root):
    #         if (root.left):
    #             xs.append(root.left.val)
    #         elif (root.left or root.right):
    #             xs.append(None)

    #         if (root.right):
    #             xs.append(root.right.val)
    #         elif (root.left or root.right):
    #             xs.append(None)

    #         self.flatten(root.left, xs)
    #         self.flatten(root.right, xs)

    def __isSymmetric(self, t1: TreeNode, t2: TreeNode):
        if (t1 == None and t2 == None): return True
        if (t1 == None or t2 == None): return False
        print(f"{t1.val} {t2.val}")
        return (t1.val == t2.val) and self.__isSymmetric(t1.left, t2.right) and self.__isSymmetric(t1.right, t2.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.__isSymmetric(root, root)

s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
res = s.isSymmetric(root)
print(res)