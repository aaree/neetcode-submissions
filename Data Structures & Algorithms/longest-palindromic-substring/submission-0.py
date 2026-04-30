class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(s,l,r):
            length=0
            string=''
            while l>=0 and r<len(s) and s[l]==s[r]:
                string=s[l:r+1]
                l-=1
                r+=1
            return string
        maxWindow=''
        for i in range(len(s)):
            newString=helper(s,i,i+1)
            if len(newString)>len(maxWindow):
                maxWindow=newString
            newString=helper(s,i,i)
            if len(newString)>len(maxWindow):
                maxWindow=newString
        return maxWindow