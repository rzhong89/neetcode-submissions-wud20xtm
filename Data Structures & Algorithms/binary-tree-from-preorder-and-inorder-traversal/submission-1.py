# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        inOrderIndex = inorder.index(preorder[0])
        leftLength = len(inorder[:inOrderIndex])
        rightLength = len(inorder[inOrderIndex + 1:])

        root.left = self.buildTree(preorder[1:1 + inOrderIndex], inorder[:inOrderIndex])
        root.right = self.buildTree(preorder[1 + inOrderIndex:], inorder[1 + inOrderIndex:])

        return root