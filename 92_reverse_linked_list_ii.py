# Definition for singly-linked list.
#class ListNode(object):
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        leftPrevious = dummy

        # Move leftPrevious to the node before the left position
        for i in range(left - 1):
            leftPrevious = leftPrevious.next
        
        # Start reversing the sublist
        prev = None
        current = leftPrevious.next
        for i in range(right - left + 1):
            tempNext = current.next
            current.next = prev
            prev = current
            current = tempNext
        
        # Connect the reversed sublist with the rest of the list
        leftPrevious.next.next = current
        leftPrevious.next = prev

        return dummy.next

#Time complexity: O(n)
#Space complexity: O(1)





        
