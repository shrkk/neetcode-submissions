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
        pointerHash = {None : None}
        curr = head
        while curr:
            pointerHash[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            pointerHash[curr].next = pointerHash[curr.next]
            pointerHash[curr].random = pointerHash[curr.random]
            curr = curr.next
        return pointerHash[head]

            
