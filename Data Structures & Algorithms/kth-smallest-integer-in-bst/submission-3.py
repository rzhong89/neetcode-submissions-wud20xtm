# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 1
        res = 0

        def dfs(root):
            nonlocal count
            nonlocal res

            if not root:
                return
            
            
            dfs(root.left)
            if res:
                return
                
            if count == k:
                res = root.val
                return
            count += 1
            dfs(root.right)

        dfs(root)
        return res