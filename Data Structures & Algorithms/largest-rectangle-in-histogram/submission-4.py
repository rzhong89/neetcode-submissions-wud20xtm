class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                area = (i - index) * height
                res = max(res, area)
                start = index
            stack.append((start, h))

        while stack:
            index, height = stack.pop()
            area = (len(heights) - index) * height
            res = max(res, area)

        return res