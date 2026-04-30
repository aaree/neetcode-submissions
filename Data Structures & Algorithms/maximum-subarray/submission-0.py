class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        L=R=0
        maxL=maxR=0
        curSum=0
        maxSum=nums[0]
        while R<len(nums):
            curSum+=nums[R]
            if curSum>maxSum:
                maxSum=curSum
                maxL,maxR=L,R
            if curSum<0:
                curSum=0
                L=R
            R+=1
        return maxSum