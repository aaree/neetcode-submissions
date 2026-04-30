class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        minCurSum=maxCurSum=0
        L=R=maxL=maxR=0
        minSum=maxSum=nums[0]
        while R<(len(nums)):
            minCurSum+=nums[R]
            maxCurSum+=nums[R]
            if minCurSum<minSum:
                minSum=minCurSum
            if maxCurSum>maxSum:
                maxSum=maxCurSum
            if minCurSum>0:
                minCurSum=0
            if maxCurSum<0:
                maxCurSum=0
            R+=1
        if maxSum < 0:
            return maxSum
        else:
            return max(maxSum,sum(nums)-minSum)