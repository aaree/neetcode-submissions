class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters=set(s)
        maxWindow=0
        for i in letters:
            r=0
            l=0
            replace=k
            while r<len(s):
                if s[r]!=i:
                    replace-=1
                while replace<0:
                    if s[l]!=i:
                        replace+=1
                    l+=1
                window=r-l+1
                maxWindow=max(window,maxWindow)
                r+=1
        return maxWindow
                    
                
        