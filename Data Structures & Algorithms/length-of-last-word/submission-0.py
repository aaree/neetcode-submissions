class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a=s.split(' ')
        b=[i for i in a if len(i)>0]
        return len(b[-1])