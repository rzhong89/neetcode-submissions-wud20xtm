class Solution:
    def isValid(self, s: str) -> bool:
        map = {'{': '}','(': ')','[': ']'}
        stack = []

        for c in s:
            if c in map:
                stack.append(c)
            elif stack and map[stack[-1]] == c:
                stack.pop()
            else:
                return False

        return True if not stack else False