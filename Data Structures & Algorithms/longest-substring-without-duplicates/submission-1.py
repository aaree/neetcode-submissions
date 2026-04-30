class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}
        l=0
        r=0
        maxWindow=0
        while r<len(s):
            seen[s[r]]=seen.get(s[r],0)+1
            while seen[s[r]]>1:
                seen[s[l]]=seen.get(s[l])-1
                l+=1
            window=r-l+1
            maxWindow=max(window,maxWindow)
            r+=1
        return maxWindow
