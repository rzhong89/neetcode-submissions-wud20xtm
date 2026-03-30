class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqToStrsMap = defaultdict(list)

        for s in strs:
            alphabet = [0] * 26
            for c in s:
                alphabet[ord(c) - ord('a')] += 1
            freqToStrsMap[tuple(alphabet)].append(s)

        return list(freqToStrsMap.values())
