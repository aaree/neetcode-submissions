class Solution:
    def countSubstrings(self, s: str) -> int:
        def helper(s,l,r):
            length=0
            cnt=0
            while l>=0 and r<len(s) and s[l]==s[r]:
                cnt+=1
                l-=1
                r+=1
            return cnt
        maxWindow=0
        for i in range(len(s)):
            newString=helper(s,i,i+1)
            maxWindow+=newString
            newString=helper(s,i,i)
            maxWindow+=newString
        return maxWindow