# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        dummy = node = ListNode()

        while curr1 and curr2:
            if curr1.val < curr2.val:
                temp = curr1
                curr1 = curr1.next
                node.next = temp
            else:
                temp = curr2
                curr2 = curr2.next
                node.next = temp
            node = node.next

        if not curr1:
            node.next = curr2
        elif not curr2:
            node.next = curr1
        return dummy.next
