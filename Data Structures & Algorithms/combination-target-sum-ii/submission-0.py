class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        combo = []
        total = 0

        def backtrack(i):
            nonlocal total

            if total == target:
                res.append(combo.copy())
                return
            
            if total > target or i >= len(candidates):
                return

            combo.append(candidates[i])
            total += candidates[i]
            backtrack(i + 1)

            combo.pop()
            total -= candidates[i]

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1)

        backtrack(0)
        return res