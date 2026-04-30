class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if nums[0]!=0:
            DP={nums[0]:1,-nums[0]:1}
        elif nums[0]==0:
            DP={nums[0]:2}
        print(DP)
        for num in range(1,len(nums)):
            i=nums[num]
            temp={}
            for key, val in DP.items():
                plus=key+i
                minus=key-i
                temp[plus]=temp.get(plus,0)+val
                temp[minus]=temp.get(minus,0)+val
            DP=temp
        if target in DP:
            return DP[target]
        else:
            return 0