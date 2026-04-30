class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        DP=[nums[0],-nums[0]]
        for num in range(1,len(nums)):
            i=nums[num]
            temp=[]
            for j in range(0,len(DP)):
                plus=DP[j]+i
                minus=DP[j]-i
                temp.append(plus)
                temp.append(minus)
            DP=temp
        cnt=0
        for i in DP:
            if i==target:
                cnt+=1
        return cnt
