class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if t=="":
            return 0
        tnum=0
        for i in s:
            if i==t[tnum]:
                tnum+=1
            if tnum==len(t):
                return 0
        return len(t)-tnum