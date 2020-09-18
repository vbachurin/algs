# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        # ld = 0
        ld = 1 + self.depth(root.left)
        rd = 1 + self.depth(root.right)
        print(f"ld = {ld}, rd = {rd}")
        if abs(ld - rd) > 1: 
            return False  
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root: TreeNode) -> int:
        if (not root):
            return 0
        else:
            ld = 1 + self.depth(root.left)
            rd = 1 + self.depth(root.right)
            print(f"I'm at {root.val}, ld = {ld}, rd = {rd}")
            return max(ld, rd)

    def sortedArrayToBST(self, nums) -> TreeNode:
        if not nums: return None
        mid = len(nums) // 2
        if nums[mid]:
            root = TreeNode(nums[mid]) 
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid+1:])
            return root    
        else:
            return None

s = Solution()
# Input:

# root2 = s.sortedArrayToBST([1,2,2,3,None,None,3,4,None,None,4])
# root2 = s.sortedArrayToBST([1,2,2,3,None])
# Output:
# true
# Expected:
# false
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(4)
root.left.left.right.left = TreeNode(44)
# root.left.right = TreeNode(10)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)
# root.right.right.right = TreeNode(20)
res = s.isBalanced(root)
print(res)
        