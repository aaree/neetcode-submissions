class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnum=set(nums)
        seen=set()
        cntd={}
        for i in nums:
            if i in seen:
                continue
            else:
                seen.add(i)
            cnt=1
            val=i
            while val-1 in setnum:
                seen.add(val-1)  
                cnt+=1
                val-=1
            lowest=val
            val=i
            while val+1 in setnum:
                seen.add(val+1)
                cnt+=1
                val+=1
            cntd[lowest]=cnt
        ans=0
        for key,val in cntd.items():
            ans=max(ans,val)
        return ans