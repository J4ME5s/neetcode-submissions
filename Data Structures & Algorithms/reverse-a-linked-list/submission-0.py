# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # empty list
        if head is None or head.next is None:
            return head

        prev = head
        curr = head.next
        prev.next = None

        while curr.next is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        curr.next = prev
        head = curr
        return head
