class Solution:
    def partition(self, head, x):
        # Dummy nodes for two lists
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)

        less = less_dummy
        greater = greater_dummy

        current = head

        while current:

            if current.val < x:
                less.next = current
                less = less.next

            else:
                greater.next = current
                greater = greater.next

            current = current.next

        # End the greater/equal list
        greater.next = None

        # Connect both lists
        less.next = greater_dummy.next

        return less_dummy.next