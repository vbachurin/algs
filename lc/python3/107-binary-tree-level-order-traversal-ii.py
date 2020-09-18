# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
  
  def levelOrderBottom(self, root: TreeNode): # -> List[List[int]]:
    res = []
    self.dfs(root, 0, res)
    return res

  def dfs(self, root, level, res):
    if root:
      if len(res) < level + 1:
        res.insert(0, [])
      res[-(level+1)].append(root.val)
      self.dfs(root.left, level + 1, res)
      self.dfs(root.right, level + 1, res)


# [1,2,3,4,null,null,5]


s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)  
root.right.right = TreeNode(5)
res = s.levelOrderBottom(root)
print(res)