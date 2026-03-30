class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        res = ""

        for length in range(1, len(s) + 1):
            for i in range(len(s) - length + 1):
                j = i + length - 1

                if length == 1:
                    dp[i][j] = True
                elif length == 2:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]

                if dp[i][j] and j - i + 1 > len(res):
                    res = s[i: j + 1]

        return res 