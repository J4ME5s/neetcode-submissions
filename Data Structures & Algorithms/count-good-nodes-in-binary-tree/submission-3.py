# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(cur, maxVal):
            if not cur:
                return 0
            good = 0
            if cur.val >= maxVal:
                good = 1
            
            maxVal = max(cur.val, maxVal)

            return good + dfs(cur.left, maxVal) + dfs(cur.right, maxVal)
        
        return dfs(root, root.val)