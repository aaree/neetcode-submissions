class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        uniqueLetters=set(list(s))
        maxWindow=0
        for let in uniqueLetters:
            l=r=0
            dupe=k
            while r<len(s):
                if s[r]!=let:
                    dupe-=1
                while dupe<0:
                    if s[l]!=let:
                        dupe+=1
                    l+=1
                window=r-l+1
                maxWindow=max(maxWindow,window)
                r+=1
        return maxWindow