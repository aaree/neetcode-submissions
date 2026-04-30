class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen={}
        cnt=0
        for i in nums:
            if i not in seen:
                seen[i]=0
            elif i in seen:
                seen[i]+=1
                cnt+=seen[i]
        return cnt