class Solution:
    def isValid(self, s: str) -> bool:
        pMap = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for c in s:
            if c in pMap:
                stack.append(c)
            else:
                if stack and c == pMap[stack[-1]]:
                    stack.pop()
                else:
                    return False

        return True if not stack else False
