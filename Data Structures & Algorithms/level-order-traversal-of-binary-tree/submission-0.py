# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def levOrder(curr, level):
            if not curr:
                return 

            if level == len(res):
                res.append([])
            res[level].append(curr.val)

            levOrder(curr.left, level + 1)
            levOrder(curr.right, level + 1)

        levOrder(root, 0)
        return res