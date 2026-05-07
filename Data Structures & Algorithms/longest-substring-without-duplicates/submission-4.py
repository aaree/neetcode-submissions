class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=r=0
        maxWindow=0
        count={}
        while r<len(s):
            count[s[r]]=count.get(s[r],0)+1
            while count[s[r]]>1:
                count[s[l]]-=1
                l+=1
            window=r-l+1
            maxWindow=max(maxWindow,window)
            r+=1
        return maxWindow