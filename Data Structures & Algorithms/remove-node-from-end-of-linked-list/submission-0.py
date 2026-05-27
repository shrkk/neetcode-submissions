# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        lenList = 0
        while curr:
            lenList += 1
            curr = curr.next

        rmIndex = lenList - n   
        if rmIndex == 0:
            return head.next
        curr = head
        itr = 0


        while curr and itr < rmIndex -1:
            curr = curr.next
            itr += 1
        curr.next = curr.next.next
        return head