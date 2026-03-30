class Solution:
    def isValid(self, s: str) -> bool:
        # if its opening push, else check for corresponding opening bracket, if its there pop, else return false
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if stack and closeToOpen[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
                
        
        return True if not stack else False
        