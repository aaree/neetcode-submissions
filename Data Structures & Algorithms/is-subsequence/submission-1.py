class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s=="":
            return True
        point=0
        for i in t:
            if i==s[point]:
                point+=1
            if point==len(s):
                return True
        return False