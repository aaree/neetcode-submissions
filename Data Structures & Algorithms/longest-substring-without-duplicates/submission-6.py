class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c={}
        l=r=0
        maxlen=0
        while r<len(s):
            c[s[r]]=c.get(s[r],0)+1
            while c[s[r]]>1:
                c[s[l]]=c[s[l]]-1
                l+=1
            maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen
