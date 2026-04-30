class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        a=len(s1)-1
        s1Count=Counter(s1)
        left=0
        for right in range(a,len(s2)):
            s2Count=Counter(s2[left:right+1])
            if s1Count==s2Count:
                return True
            left+=1
        return False