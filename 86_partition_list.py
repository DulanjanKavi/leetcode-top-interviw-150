# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """

        dummy1= current1 = ListNode(0)
        dummy2= current2 = ListNode(0)

        current = head

        while current:
            if current.val<x:
                current1.next=current
                current1= current1.next
            
            else:
                current2.next=current
                current2=current2.next

            current=current.next


        current1.next=dummy2.next
        current2.next=None
        return dummy1.next
    
#Time complexity: O(n)
#Space complexity: O(1)
        
