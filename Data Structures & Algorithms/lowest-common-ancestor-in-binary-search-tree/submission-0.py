# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        currRoot = root

        while (currRoot.val > p.val and currRoot.val > q.val) or (currRoot.val < p.val and currRoot.val < q.val):
            if (currRoot.val > p.val and currRoot.val > q.val):
                # go left
                currRoot = currRoot.left
            elif (currRoot.val < p.val and currRoot.val < q.val):
                # go right
                currRoot = currRoot.right
        return currRoot