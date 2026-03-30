class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        s = []
        opens = 0
        closes = 0

        def backtrack():
            nonlocal opens
            nonlocal closes

            if opens == closes == n:
                res.append("".join(s))
                return
            
            if opens < n:
                s.append("(")
                opens += 1
                backtrack()
                s.pop()
                opens -= 1

            if closes < opens:
                s.append(")")
                closes += 1
                backtrack()
                s.pop()
                closes -= 1

        backtrack()
        return res
            