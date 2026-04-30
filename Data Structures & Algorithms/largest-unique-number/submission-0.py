class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        seen={}
        max_value=-1
        for i in nums:
            seen[i]=seen.get(i,0)+1
        maxVal=-1
        for key, val in seen.items():
            if val==1:
                maxVal=max(maxVal,key)
        return maxVal
                