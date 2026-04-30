class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt={}
        l=r=0
        maxWindow=0
        window=0
        while r<len(s):
            cnt[s[r]]=cnt.get(s[r],0)+1
            while cnt[s[r]]>1:
                cnt[s[l]]=cnt.get(s[l],0)-1
                l+=1
            window=r-l+1
            maxWindow=max(maxWindow,window)
            r+=1
        return maxWindow