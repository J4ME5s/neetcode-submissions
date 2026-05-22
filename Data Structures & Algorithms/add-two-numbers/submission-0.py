# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        curr = dummy

        while l1 or l2 or carry:
            curr.next = ListNode()
            curr = curr.next
            l1val = 0
            l2val = 0
            if l1 is not None:
                l1val = l1.val
                l1 = l1.next
            if l2 is not None:
                l2val = l2.val
                l2 = l2.next
            
            newVal = l1val + l2val + carry
            carry = int(newVal / 10)
            remainder = newVal % 10
            curr.val = remainder
        
        return dummy.next

