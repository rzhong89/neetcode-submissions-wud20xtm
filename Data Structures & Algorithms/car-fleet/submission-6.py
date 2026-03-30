class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        for i in range(len(pair)):
            time2 = (target - pair[i][0]) / pair[i][1]
            if stack and stack[-1] >= time2:
                continue

            stack.append(time2)
        
        return len(stack)
            
            
