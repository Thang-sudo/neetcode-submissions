# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Merge Two Sorted Lists — dummy head + tail pointer
        #
        # IDEA: Build one sorted list by repeatedly picking the smaller head node.
        #   Use a DUMMY anchor so you never special-case "the first node," and a
        #   separate TAIL pointer that always points at the last node placed.
        #
        # STEPS:
        #   dummy = ListNode(); tail = dummy
        #   while both lists non-empty:
        #       pick the list with the smaller head
        #       tail.next = that node          # link it in
        #       advance that list (list = list.next)   # <-- easy to forget! else infinite loop
        #       tail = tail.next               # move tail forward
        #   tail.next = whichever list still has nodes   # one is empty, attach the rest
        #   return dummy.next                  # real head (skip the dummy)
        #
        # WHY IT WORKS: both inputs are already sorted, so the next-smallest overall
        #   is always one of the two current heads. Splicing existing nodes = O(1) extra
        #   space (no new nodes except the dummy).
        #
        # COMPLEXITY: O(n + m) time, O(1) space.
        #
        # GOTCHAS:
        #   - advance the consumed list each step (missing it => infinite loop)
        #   - only ONE leftover attach needed (the other list is empty)
        #   - return dummy.next, NOT dummy
        dummyNode = ListNode()
        tail = dummyNode
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2
        return dummyNode.next
        