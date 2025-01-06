# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy= ListNode()
        dummy.next=head

        pointer1=dummy

        pointer2=dummy

        i=0

        while i<n+1:
            pointer2=pointer2.next
            i+=1
        
        while pointer2:
            pointer2=pointer2.next
            pointer1=pointer1.next
        
        pointer1.next=pointer1.next.next
        
        return dummy.next

#time complexity: O(n)
#space complexity: O(1)
