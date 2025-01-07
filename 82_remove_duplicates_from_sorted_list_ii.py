# Definition for singly-linked list.
#class ListNode(object):
#    def __init__(self, val=0, next=None):
#       self.val = val
#       self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head

        while current:
            # Check for duplicates
            if current.next and current.val == current.next.val:
                # Skip all nodes with the same value
                while current.next and current.val == current.next.val:
                    current = current.next
                # Connect prev node to the node after the last duplicate
                prev.next = current.next
            else:
                # Move prev pointer to current node
                prev = prev.next
            # Move current pointer to the next node
            current = current.next
        
        return dummy.next

#Time complexity: O(n)
#Space complexity: O(1)
