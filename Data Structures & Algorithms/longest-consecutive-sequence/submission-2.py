class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnum=set(nums)
        seen=set()
        longest=0
        for i in setnum:
            if i in seen:
                continue
            length=0
            val=i
            while val in setnum:
                length+=1
                val+=1
                seen.add(val)
            longest=max(longest,length)
        return longest
                
