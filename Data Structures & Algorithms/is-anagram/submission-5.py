class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = Counter(s)
        tMap = Counter(t)

        if sMap == tMap:
            return True
        else:
            return False

