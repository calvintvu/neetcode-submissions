# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        cur = dummyHead = ListNode(0, head)

        length = 0
        counter = head
        while counter:
            length += 1
            counter = counter.next
        
        index_to_remove = length - n
        print(index_to_remove)
        
        for i in range(index_to_remove):
            cur = cur.next
        cur.next = cur.next.next
        
        return dummyHead.next
        print(cur.val)