class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2==1:
            return False
        target=sum(nums)/2
        total=set()
        for num in nums:
            if num==target:
                return True
            temp=set()
            for val in total:
                val+=num
                if val==target:
                    return True
                temp.add(val)
            total.add(num)
            total.update(temp)
        return False
