"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        if not head:
            return None
        
        current=head
        old_to_new={}

        while current:
            node = Node(x = current.val)
            old_to_new[current] = node
            current = current.next

        current = head
        while current:
            new_node = old_to_new[current]
            new_node.next = old_to_new[current.next] if current.next else None
            new_node.random = old_to_new[current.random] if current.random else None
            current = current.next

        return old_to_new[head]

#Time complexity: O(n)
#Space complexity: O(n)



        
