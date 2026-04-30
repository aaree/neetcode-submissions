class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        ana={}
        ana2={}
        for i in range(len(s)):
            ana[s[i]]=ana.get(s[i],0)+1
            ana2[t[i]]=ana2.get(t[i],0)+1
        return ana==ana2