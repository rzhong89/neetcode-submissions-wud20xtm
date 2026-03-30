class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left = 0
        right = len(height) - 1
        leftMax = height[left]
        rightMax = height[right]

        while left < right:
            if leftMax > rightMax:
                right -= 1
                rightMax = max(rightMax, height[right])
                res += rightMax - height[right]
            else:
                left += 1
                leftMax = max(leftMax, height[left])
                res += leftMax - height[left]

        return res