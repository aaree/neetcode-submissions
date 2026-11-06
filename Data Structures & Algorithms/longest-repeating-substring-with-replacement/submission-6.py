class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=r=0
        maxlen=0
        replace=k
        letters=set(s)
        for letter in letters:
            length=0
            l=r=0
            replace=k
            while r<len(s):
                if s[r]==letter:
                    length+=1
                else:
                    replace-=1
                    length+=1
                while replace<0:
                    if s[l]!=letter:
                        replace+=1
                    l+=1
                    length-=1
                maxlen=max(length,maxlen)
                r+=1
        return maxlen

