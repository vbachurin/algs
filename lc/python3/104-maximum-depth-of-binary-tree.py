# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
      if not root: return 0
      if not root.left: return 1 + self.minDepth(root.right)
      elif not root.right: return 1 + self.minDepth(root.left)
      else: return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

  #   3
  #  / \
  # 9  20
  #   /  \
  #  15   7
s = Solution()
# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(20)
res = s.minDepth(root)
print(res)