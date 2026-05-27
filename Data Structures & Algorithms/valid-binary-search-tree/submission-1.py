# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidHelper(curr, left, right):

            if not curr:
                return True
            if not (left < curr.val < right):
                return False
            return isValidHelper(curr.left, left, curr.val) and isValidHelper(curr.right, curr.val, right)

        return isValidHelper(root, float("-inf"), float("inf"))