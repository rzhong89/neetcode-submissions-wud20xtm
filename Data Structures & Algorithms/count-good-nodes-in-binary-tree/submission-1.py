# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(root, maxBefore):
            if not root:
                return

            nonlocal res

            if root.val >= maxBefore:
                res += 1

            dfs(root.left, max(maxBefore, root.val))
            dfs(root.right, max(maxBefore, root.val))

        dfs(root, float('-inf'))
        return res