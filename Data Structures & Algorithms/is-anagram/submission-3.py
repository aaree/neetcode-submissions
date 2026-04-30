class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        one={}
        two={}
        for i in s:
            one[i]=one.get(i,0)+1
        for i in t:
            two[i]=two.get(i,0)+1
        return one==two