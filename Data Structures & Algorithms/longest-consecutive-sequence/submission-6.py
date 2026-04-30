class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique=set(nums)
        cnt=0
        max_cnt=0
        for i in nums:
            if (i-1) in nums:
                continue
            else:
                temp=i
                while temp in nums:
                    cnt+=1
                    temp+=1
                max_cnt=max(max_cnt,cnt)
                cnt=0
        return max_cnt