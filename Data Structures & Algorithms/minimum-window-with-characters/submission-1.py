class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = 0
        left = 0
        tFreq = {}

        for c in t:
            tFreq[c] = 1 + tFreq.get(c, 0)

        window = {}
        have = 0
        need = len(tFreq)
        res = [-1, -1]
        resLen = float('inf')

        for right in range(len(s)):
                
            window[s[right]] = 1 + window.get(s[right], 0)

            if s[right] in tFreq and window[s[right]] == tFreq[s[right]]:
                have += 1

            while have == need:
                if right - left + 1 < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                window[s[left]] -= 1
                
                if s[left] in tFreq and window[s[left]] < tFreq[s[left]]:
                    have -= 1

                left += 1

        left, right = res

        return s[left: right + 1] if resLen != float('inf') else ""
                
        