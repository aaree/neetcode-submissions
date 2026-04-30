class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        l=0
        r=len(s)-1
        while r>l:
            while r>l and not s[r].isalnum():
                r-=1
            while r>l and not s[l].isalnum():
                l+=1
            if s[l]!=s[r]:
                return False
            r-=1
            l+=1
        return True