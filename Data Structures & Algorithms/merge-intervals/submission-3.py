class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                newInterval = [res[-1][0],max(intervals[i][1], res[-1][1])]
                res.pop()
                res.append(newInterval)
            else:
                res.append(intervals[i])
        
        return res

