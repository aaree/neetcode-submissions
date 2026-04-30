class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxCNT=0
        cnt=0
        seen={}
        allVal=set(nums)
        for i in nums:
            if i in seen:
                continue
            temp=i
            while temp in allVal:
                seen[i]=seen.get(i,0)+1
                temp+=1
                if temp in seen:
                    seen[i]+=seen[temp]
                    break
        for key,val in seen.items():
            maxCNT=max(val,maxCNT)
        return maxCNT