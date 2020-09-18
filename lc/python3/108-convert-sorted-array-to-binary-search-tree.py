# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        if not nums: return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

    def printTree(self, root, res):
        if root:
            res.append(root.val)
        else:
            res.append(None)
        print(res)
        if root.left: 
            self.printTree(root.left, res)
            print("l")
            print(res)
        if root.right: 
            self.printTree(root.right, res)
            print("r")
            print(res)


s = Solution()
nums = [-20,-10,-3,0,5,9, 19]
root = s.sortedArrayToBST(nums)
print(s.printTree(root, []))

