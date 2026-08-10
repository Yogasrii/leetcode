class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []

        def build(start, end):
            result = []

            # No nodes
            if start > end:
                return [None]

            # Try every value as root
            for root in range(start, end + 1):

                left_trees = build(start, root - 1)
                right_trees = build(root + 1, end)

                # Combine every left and right subtree
                for left in left_trees:
                    for right in right_trees:

                        node = TreeNode(root)
                        node.left = left
                        node.right = right

                        result.append(node)

            return result

        return build(1, n)