class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen={}
        allVals=set(nums)
        maxSeq=0
        seq=0
        for i in nums:
            if i in seen:
                continue
            else:
                curr=i
                while (curr in allVals and curr not in seen):
                    seq+=1
                    seen[i]=seq
                    curr+=1                    
                if curr in allVals:
                    seq+=seen[curr]
                    seen[i]=seq
                if seq>maxSeq:
                    maxSeq=seq
                seq=0
        return maxSeq
