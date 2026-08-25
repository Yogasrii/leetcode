class Solution:
    def insertionSortList(self, head):
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        current = head

        while current:
            next_node = current.next

            # Find the correct position
            prev = dummy

            while prev.next and prev.next.val < current.val:
                prev = prev.next

            # Insert current
            current.next = prev.next
            prev.next = current

            current = next_node

        return dummy.next