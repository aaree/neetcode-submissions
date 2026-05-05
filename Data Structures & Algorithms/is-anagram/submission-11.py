class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c={}
        d={}
        for i in s:
            c[i]=c.get(i,0)+1
        for i in t:
            d[i]=d.get(i,0)+1
        return c==d