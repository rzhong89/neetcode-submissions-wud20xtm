class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.isPalindrome(s[i:j + 1]):
                    if len(s[i:j + 1]) > len(res):
                        res = s[i:j + 1]
        
        return res
    
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1

        return True