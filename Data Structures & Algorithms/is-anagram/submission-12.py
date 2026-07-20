class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap={}
        tmap={}
        for i in s:
            smap[i]=smap.get(i,0)+1
        for j in t:
            tmap[j]=tmap.get(j,0)+1
        return smap==tmap