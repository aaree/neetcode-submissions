class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sets={}
        sett={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            sets[s[i]]=sets.get(s[i],0)+1
            sett[t[i]]=sett.get(t[i],0)+1
        return sets==sett