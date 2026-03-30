class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        for i in range(len(pair)):
            time2 = (target - pair[i][0]) / pair[i][1]
            if stack and time2 <= stack[-1]:
                continue

            stack.append(time2)
        
        return len(stack)
            
            
