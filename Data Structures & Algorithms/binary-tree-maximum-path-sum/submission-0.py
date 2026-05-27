class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = -float("inf")   # global tracker

        def dfs(node):
            if not node:
                return 0

            # Compute max contribution from left & right
            left = max(dfs(node.left), 0)   # ignore negatives
            right = max(dfs(node.right), 0)

            # Update global maxSum if path goes through this node
            self.maxSum = max(self.maxSum, node.val + left + right)

            # Return the best contribution upwards (only one side allowed)
            return node.val + max(left, right)

        dfs(root)
        return self.maxSum
