class BSTIterator:

    def __init__(self, root):
        self.values = []
        self.index = 0

        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            self.values.append(node.val)
            inorder(node.right)

        inorder(root)

    def next(self):
        value = self.values[self.index]
        self.index += 1
        return value

    def hasNext(self):
        return self.index < len(self.values)