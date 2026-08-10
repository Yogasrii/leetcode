class Solution:
    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head

        # Dummy node handles the case where left == 1
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        # Move prev to the node before left
        for _ in range(left - 1):
            prev = prev.next

        # Reverse the required portion
        current = prev.next

        for _ in range(right - left):
            next_node = current.next

            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next