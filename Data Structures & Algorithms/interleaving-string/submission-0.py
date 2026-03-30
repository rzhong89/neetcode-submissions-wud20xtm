class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}

        def dfs(i, j, k):
            if k == len(s3):
                return (i == len(s1) and j == len(s2))

            if (i, j, k) in memo:
                return memo[(i, j, k)]

            if i < len(s1) and s1[i] == s3[k]:
                if dfs(i + 1, j, k + 1):
                    memo[(i, j, k)] = True
                    return True

            if j < len(s2) and s2[j] == s3[k]:
                if dfs(i, j + 1, k + 1):
                    memo[(i, j, k)] = True
                    return True

            memo[(i, j, k)] = False
            return False
        
        return dfs(0, 0, 0)