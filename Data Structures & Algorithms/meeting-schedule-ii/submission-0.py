"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        cnt=0
        ans=[]
        for i in intervals:
            ans.append((i.start,1))
            ans.append((i.end,-1))
        max_cnt=0
        ans.sort()
        for i in ans:
            cnt+=i[1]
            max_cnt=max(max_cnt,cnt)
        return max_cnt