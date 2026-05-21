# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # sort and merge in pairs
        # add to one list
        # skip over empty lists

        def mergeTwoLists(l1, l2):
            list1 = l1
            list2 = l2
            head = ListNode()
            tempTail = head
            while list1 and list2:
                if list1.val <= list2.val:
                    tempTail.next = list1
                    list1 = list1.next
                else:
                    tempTail.next = list2
                    list2 = list2.next
                tempTail = tempTail.next
            # add rest of list
            if list1:
                tempTail.next = list1
            elif list2:
                tempTail.next = list2
            return head.next
        
        # remove empty lists
        lists = [l for l in lists if l]

        if not lists:
            return None
        
        while len(lists) > 1:
            merged = []
            i = 0
            while i < len(lists):
                left = lists[i]
                right = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(mergeTwoLists(left, right))
                i += 2
            lists = merged
        return lists[0]
        