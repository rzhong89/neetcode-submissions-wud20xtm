class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        res = 0
        left = 0

        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[left])
                left += 1

            window.add(s[r])
            length = r - left + 1
            res = max(res, length)

        return res