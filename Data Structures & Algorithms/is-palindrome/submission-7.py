import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while r>l:
            while l<len(s) and not s[l].isalnum():
                l+=1
            while r>=0 and not s[r].isalnum():
                r-=1
            if r<=l:
                break
            if s[l].lower()!=s[r].lower():
                return False
            r-=1
            l+=1
        return True