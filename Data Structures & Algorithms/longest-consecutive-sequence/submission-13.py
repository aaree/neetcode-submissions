class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        allValues=set(nums)
        seen=set()
        maxCount=0
        for num in nums:
            curr=num
            if curr not in seen:
                cnt=1
                while curr in allValues:
                    curr+=1
                    if curr in allValues:
                        cnt+=1
                    seen.add(curr)
                maxCount=max(cnt,maxCount)
            else:
                continue
        return maxCount