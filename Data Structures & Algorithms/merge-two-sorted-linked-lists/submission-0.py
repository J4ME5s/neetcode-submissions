# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (list1 == None and list2 == None) or (list2 == None):
            return list1
        elif list1 == None:
            return list2
        
        head = ListNode()
        currList1 = list1
        currList2 = list2
        tail = head

        while currList1 is not None and currList2 is not None:
            if currList1.val <= currList2.val:
                tail.next = currList1
                currList1 = currList1.next
            elif currList1.val > currList2.val:
                tail.next = currList2
                currList2 = currList2.next
            tail = tail.next
        
        if currList1 is None:
            tail.next = currList2
        elif currList2 is None:
            tail.next = currList1
        return head.next