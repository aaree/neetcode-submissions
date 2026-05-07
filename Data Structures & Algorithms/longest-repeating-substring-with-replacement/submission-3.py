class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        allLetters=set(list(s))
        maxWindow=0
        for let in allLetters:
            l=r=0
            cnt=0
            temp=k
            while r<len(s):
                if s[r]==let:
                    cnt+=1
                    r+=1
                else:
                    while temp==0:
                        if s[l]!=let:
                            temp+=1
                        cnt-=1
                        l+=1
                    if temp>0:
                        cnt+=1
                        temp-=1
                        r+=1
                maxWindow=max(maxWindow,r-l)
        return maxWindow
