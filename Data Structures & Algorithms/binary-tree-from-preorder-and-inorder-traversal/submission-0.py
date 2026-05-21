# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        rootIndex = 0
        while inorder[rootIndex] != root.val:
            rootIndex += 1
        
        leftInorder = inorder[:rootIndex]
        rightInorder = inorder[rootIndex+1:]

        leftPreorder = preorder[1:1+len(leftInorder)]
        rightPreorder = preorder[len(leftInorder) + 1:]

        root.left = self.buildTree(leftPreorder, leftInorder)
        root.right = self.buildTree(rightPreorder, rightInorder)

        return root
