# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        Use TFS to calculate heights of left and right subtrees, 
        and then also update the global variable that is a boolean 
        for is balanced. 
        '''
        res = True

        def dfs(root):
            nonlocal res

            if not root:
                return 0

            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)

            if abs(rightHeight - leftHeight) > 1:
                res = False

            return 1 + max(leftHeight, rightHeight)

        dfs(root)

        return res



