class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total={}
        if nums[0]==0:
            total[0]=2
        else:
            total[nums[0]]=1
            total[-nums[0]]=1
        cnt=0
        for i in range(1,len(nums)):
            num=nums[i]
            temp={}
            for key, val in total.items():
                k1=key+num
                k2=key-num
                temp[k1]=temp.get(k1,0)+val
                temp[k2]=temp.get(k2,0)+val
            total=temp
        print(total)
        if target not in total:
            return 0
        return total[target]
                