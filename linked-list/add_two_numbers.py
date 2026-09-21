# =========================
# LeetCode #2 - Add Two Numbers
# =========================

class Solution:
    def addTwoNumbers(self, l1, l2):

        # Create a dummy node to start the answer list
        dummy = ListNode(0)

        # This pointer will build our answer list
        current = dummy

        # Start with no carry
        carry = 0

        # Continue while either list has a node
        # or there is still a carry
        while l1 or l2 or carry:

            # Get the value from l1
            if l1:
                value1 = l1.val
            else:
                value1 = 0

            # Get the value from l2
            if l2:
                value2 = l2.val
            else:
                value2 = 0

            # Add both values and the carry
            total = value1 + value2 + carry

            # Get the digit that should be stored
            digit = total % 10

            # Get the carry for the next position
            carry = total // 10

            # Create a new node with the digit
            current.next = ListNode(digit)

            # Move current to the new node
            current = current.next

            # Move l1 to the next node
            if l1:
                l1 = l1.next

            # Move l2 to the next node
            if l2:
                l2 = l2.next

        # Return the first actual node
        return dummy.next
