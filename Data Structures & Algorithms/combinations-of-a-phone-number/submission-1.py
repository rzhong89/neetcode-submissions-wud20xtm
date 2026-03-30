class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "" or not digits:
            return []

        res = []
        s = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i):
            if len(s) == len(digits):
                res.append("".join(s))
                return

            for c in digitToChar[digits[i]]:
                s.append(c)
                backtrack(i + 1)
                s.pop()

        backtrack(0)
        return res