class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxNum=10
        maxCnt=0
        cnt=0
        for i,val in enumerate(nums):
            print(maxNum)
            if val!=maxNum:
                maxNum=val
                if val==1:
                    cnt=1
                    if cnt>maxCnt:
                        maxCnt=cnt
            elif val==maxNum:
                if val==1:
                    cnt+=1
                    if cnt>maxCnt:
                        maxCnt=cnt
        return maxCnt        
