"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)

        if len(intervals) <= 1:
            return True

        # iterate and check 2 condtions
        for i in range(1, len(intervals)):
            # is if start time of i < end time of i - 1
            if intervals[i].start < intervals[i - 1].end:
                return False
            
        return True