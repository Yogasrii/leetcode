class Solution:
    def sortedListToBST(self, head):

        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)

        # Find middle node
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Disconnect left half
        prev.next = None

        # slow is the middle node
        root = TreeNode(slow.val)

        # Build left subtree
        root.left = self.sortedListToBST(head)

        # Build right subtree
        root.right = self.sortedListToBST(slow.next)

        return root