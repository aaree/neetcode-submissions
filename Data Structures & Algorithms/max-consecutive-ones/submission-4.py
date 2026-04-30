class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCnt=0
        cnt=0
        for i,val in enumerate(nums):
            if val==1:
                cnt+=1
                if cnt>maxCnt:
                    maxCnt=cnt
            elif val==0:
                cnt=0
        return maxCnt        
