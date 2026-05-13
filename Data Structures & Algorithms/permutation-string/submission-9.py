class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        if s1==s2:
            return True
        l=r=0
        s1Arr=[0]*26
        s2Arr=[0]*26
        for i in s1:
            s1Arr[ord(i)-ord('a')]+=1
        while r<len(s2):
            s2Arr[ord(s2[r])-ord('a')]+=1
            while (r-l+1)>len(s1):
                s2Arr[ord(s2[l])-ord('a')]-=1
                l+=1
            if s2Arr==s1Arr:
                return True
            r+=1
        return False
