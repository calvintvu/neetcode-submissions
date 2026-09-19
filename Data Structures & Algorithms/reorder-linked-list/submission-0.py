# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow will be middle of list
        # now we reverse second half

        curr = slow.next
        prev = slow.next = None
        while curr:
            next_ptr = curr.next
            curr.next = prev
            prev = curr
            curr = next_ptr
        
        # prev is head of second list now

        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
        
