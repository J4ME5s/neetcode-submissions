# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        curr = head
        length = 1
        # get length of Linked List
        while curr.next is not None:
            length += 1
            curr = curr.next
        
        # edge case
        if length == n:
            return head.next

        currLen = length
        pre = None
        curr = head
        post = curr.next
        while currLen != n:
            post = post.next
            temp = curr
            curr = curr.next
            pre = temp
            currLen -= 1
        curr.next = None
        pre.next = post
        return head