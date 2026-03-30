class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap(freqlist:list of strings)
        hashMap = defaultdict(list)

        # loop thru strings and create a map for each str and 
        # place the actual string in the hashMap with 
        # the freqMap as the key

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            hashMap[tuple(count)].append(s)

        return list(hashMap.values())
