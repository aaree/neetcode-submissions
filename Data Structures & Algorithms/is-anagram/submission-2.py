class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicS={}
        dicT={}
        for i in s:
            dicS[i]=dicS.get(i,0)+1
        for i in t:
            dicT[i]=dicT.get(i,0)+1
        return dicS==dicT