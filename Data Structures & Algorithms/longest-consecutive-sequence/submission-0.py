class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s_nums=set(nums)
        begin=set()
        for i in nums:
            if i-1 not in s_nums:
                begin.add(i)
        total_cnt=0
        for i in begin:
            cnt=1
            val=i
            while val in s_nums:
                val+=1
                if val in s_nums:
                    cnt+=1
            total_cnt=max(total_cnt,cnt)
        return total_cnt