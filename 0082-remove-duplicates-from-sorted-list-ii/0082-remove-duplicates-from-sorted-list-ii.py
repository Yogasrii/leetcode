class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        current = head

        while current:

            # Check if current value is duplicated
            if current.next and current.val == current.next.val:

                duplicate_value = current.val

                # Skip all nodes with the duplicate value
                while current and current.val == duplicate_value:
                    current = current.next

                prev.next = current

            else:
                # No duplicate, move prev forward
                prev = current
                current = current.next

        return dummy.next