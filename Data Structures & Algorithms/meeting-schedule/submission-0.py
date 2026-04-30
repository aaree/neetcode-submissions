"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        ans=[]
        for i in intervals:
            ans.append((i.start,1))
            ans.append((i.end,-1))
        ans.sort()
        cnt=0
        for i in ans:
            cnt+=i[1]
            if cnt>1:
                return False
        return True