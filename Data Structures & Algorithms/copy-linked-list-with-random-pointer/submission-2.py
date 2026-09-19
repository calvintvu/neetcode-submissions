"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # default in case random points to None
        oldToCopy = {None: None}

        cur = head
        while cur:
            # create the new node with just the value
            copy = Node(cur.val)
            # map old node to new node
            oldToCopy[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            # get new node
            copy = oldToCopy[cur]
            # use mapping of old node to new node to find next copied node
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        
        return oldToCopy[head]