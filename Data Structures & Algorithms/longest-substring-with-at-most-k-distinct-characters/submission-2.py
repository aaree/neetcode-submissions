class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k==0:
            return 0
        d={}
        l=r=0
        maxS=0
        while r<len(s):
            d[s[r]]=d.get(s[r],0)+1
            while len(d)>k:
                d[s[l]]-=1
                if d[s[l]]==0:
                    del d[s[l]]
                l+=1
            length=r-l+1
            maxS=max(maxS,length)
            r+=1
        return maxS