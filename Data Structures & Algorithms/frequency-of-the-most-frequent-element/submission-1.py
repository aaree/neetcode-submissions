class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        elements=set(nums)
        maxCNT=0
        for val in elements:
            cnt=0
            temp=k
            nums.sort(key=lambda x:abs(x-val))
            for i,num in enumerate(nums):
                if num==val:
                    cnt+=1
                else:
                    if num<val:
                        temp-=abs(num-val)
                        if temp>=0:
                            cnt+=1
            maxCNT=max(cnt,maxCNT)
        return maxCNT


