class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s1={}
        t1={}
        for i, val in enumerate(s):
            s1[val]=s1.get(val,0)+1
        for j, v in enumerate(t):
            t1[v]=t1.get(v,0)+1
        return s1==t1