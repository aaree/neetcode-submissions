class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        cnt=0
        ans=[]
        for i in intervals:
            if len(ans)==0:
                ans.append(i)
            else:
                if ans[-1][1]>i[0]:
                    cnt+=1
                else:
                    ans.append(i)
        return cnt