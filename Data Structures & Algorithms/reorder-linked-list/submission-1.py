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
        
        # at this point the slow pointer is halfway
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # 1 -> 2 -> None
        # None <- 3 <- 4

        first, second = head, prev
        while first and second:
            tmpf = first.next
            tmps = second.next
            first.next = second
            second.next = tmpf 
            first = tmpf
            second = tmps

