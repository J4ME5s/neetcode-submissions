# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cur = root
        good = 1

        def method(node, val):
            nonlocal good
            if node.val >= val:
                good += 1
            maxVal = max(node.val, val)
            
            if node.left:
                method(node.left, maxVal)
            if node.right:
                method(node.right, maxVal)

        if cur.left:
            method(cur.left, cur.val)
        if cur.right:
            method(cur.right, cur.val)
        
        return good
        


