# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def goodHelper(curr : TreeNode, maxVal : int, counter : int) -> int:
            if not curr:
                return 0
            if curr.val >= maxVal:
                maxVal = curr.val
                counter = 1
            else:
                counter = 0
            return counter + goodHelper(curr.left, maxVal, counter) + goodHelper(curr.right, maxVal, counter)
        return goodHelper(root, root.val, 0)


            