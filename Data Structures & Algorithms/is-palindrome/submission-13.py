class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while r>l:
            while (s[r]==' ' or not s[r].isalnum()) and r>l:
                r-=1
            while (s[l]==' ' or not s[l].isalnum()) and l<r:
                l+=1
            if l>r:
                return True
            elif s[r].lower()!=s[l].lower():
                return False
            l+=1
            r-=1
        return True