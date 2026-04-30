class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS={}
        countT={}
        for i in s:
            countS[i]=countS.get(i,0)+1
        for i in t:
            countT[i]=countT.get(i,0)+1
        return countS==countT