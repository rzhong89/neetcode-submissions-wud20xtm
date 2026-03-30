# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
    
        def dfs(root):
            nonlocal res

            if not root:
                return 0
            
            split = root.val + max(dfs(root.left), 0) + max(dfs(root.right), 0)
            res = max(res, split)

            return max(root.val + dfs(root.left), root.val + dfs(root.right), root.val)

        dfs(root)
        return res