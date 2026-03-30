class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(i):
            if i == len(s):
                return True

            if i in memo:
                return memo[i]
            
            for word in wordDict:
                if i + len(word) <= len(s) and s[i:].startswith(word):
                    memo[i] = dfs(i + len(word))
                    if memo[i]:
                        return True
            
            return False
        
        return dfs(0)

            
                
