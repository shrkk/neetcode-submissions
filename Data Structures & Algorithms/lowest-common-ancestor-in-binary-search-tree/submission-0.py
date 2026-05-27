# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def bs(curr, p, q):
            if not curr:
                return None
            if curr.val < p.val and curr.val < q.val:
                return bs(curr.right, p, q)
            elif curr.val > p.val and curr.val > q.val:
                return bs(curr.left, p, q)
            else:
                return curr   
        return bs(root, p, q)

            
