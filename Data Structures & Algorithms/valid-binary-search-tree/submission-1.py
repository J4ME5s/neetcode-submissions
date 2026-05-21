# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue = [(root, -1001, 1001)]
        while queue:
            curr, min, max = queue.pop(0)
            if not (min < curr.val < max):
                return False
            if curr.left is not None:
                queue.append((curr.left, min, curr.val))
            if curr.right is not None:
                queue.append((curr.right, curr.val, max))
        return True