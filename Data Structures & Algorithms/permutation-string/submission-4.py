class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        l=0
        r=len(s1)
        c1=Counter(s1)
        c2=Counter(s2[l:r])
        if c1==c2:
            return True
        while r<len(s2):
            c2[s2[l]]=c2.get(s2[l],0)-1
            if c2[s2[l]]<=0:
                del c2[s2[l]]
            c2[s2[r]]=c2.get(s2[r],0)+1
            print(c2)
            if c1==c2:
                return True
            r+=1
            l+=1
        return False
