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
        if not head:
            return None
        nodeMap = {None: None}
        curr = head
        while curr:
            newNode = Node(curr.val)
            nodeMap[curr] = newNode
            curr = curr.next
        
        curr = head
        newHead = nodeMap[curr]
        while curr:
            newNode = nodeMap[curr]
            newNode.next = nodeMap[curr.next]
            newNode.random = nodeMap[curr.random]
            curr = curr.next
        return newHead


        