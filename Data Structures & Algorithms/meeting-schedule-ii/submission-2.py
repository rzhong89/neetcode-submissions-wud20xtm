"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startTimes = sorted([i.start for i in intervals])
        endTimes = sorted([i.end for i in intervals])

        res = count = 0
        start = end = 0

        while start < len(startTimes):
            if startTimes[start] < endTimes[end]:
                start += 1
                count += 1
            elif startTimes[start] >= endTimes[end]:
                end += 1
                count -= 1

            res = max(res, count)

        return res
    