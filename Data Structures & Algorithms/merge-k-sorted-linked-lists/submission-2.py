# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def mergeTwoSortedLists(list1: Optional[ListNode], list2: Optional[ListNode]):
            merged = ListNode()
            dummy = merged
            curr1, curr2 = list1, list2
            while curr1 and curr2:
                if curr1.val < curr2.val:
                    merged.next = curr1
                    curr1 = curr1.next
                else:
                    merged.next = curr2
                    curr2 = curr2.next
                merged = merged.next
            if curr1:
                merged.next = curr1
            if curr2:
                merged.next = curr2
            return dummy.next

        if not lists:
            return None

        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged_lists.append(mergeTwoSortedLists(l1, l2))
            lists = merged_lists
            
        return lists[0]
