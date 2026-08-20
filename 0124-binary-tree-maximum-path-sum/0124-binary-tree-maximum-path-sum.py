class Solution:
    def maxPathSum(self, root):
        self.maximum = float('-inf')

        def dfs(node):
            if node is None:
                return 0

            # Maximum contribution from left and right
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # Path passing through current node
            current_path = left + node.val + right

            # Update global maximum
            self.maximum = max(self.maximum, current_path)

            # Return maximum one-sided path
            return node.val + max(left, right)

        dfs(root)

        return self.maximum