class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # create hashmap of charcter to last index
        lastIndexMap = {}

        for i in range(len(s)):
            lastIndexMap[s[i]] = i

        res = []
        size = end = 0
        
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndexMap[c])

            if i == end:
                res.append(size)
                size = 0

        return res
            
