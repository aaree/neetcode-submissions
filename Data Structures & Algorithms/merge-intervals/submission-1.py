class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans=[]
        intervals.sort()
        for i in intervals:
            if len(ans)==0:
                ans.append(i)
            else:
                if ans[-1][1]>=i[0]:
                    ans[-1][1]=max(ans[-1][1],i[1])
                else:
                    ans.append(i)
        return ans