class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            freqMap[n] = 1 + freqMap.get(n, 0)
        for num, count in freqMap.items():
            freq[count].append(num)

        res = []
        i = len(freq) - 1
        while len(res) != k and i > 0:
            for n in freq[i]:
                res.append(n)
            i -= 1
        return res

        