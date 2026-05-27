# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = head
        counter = 0
        while dummy:
            dummy = dummy.next
            counter += 1
        if counter < k:
            return head
        
        
        prev, curr = None, head
        

        for x in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        head.next = self.reverseKGroup(curr, k)
        return prev

    