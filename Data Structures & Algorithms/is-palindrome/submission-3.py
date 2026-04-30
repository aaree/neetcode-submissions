class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        while right>left:
            if not s[right].isalnum():
                while right>left and not s[right].isalnum():
                    right-=1
            if not s[left].isalnum():
                while right>left and not s[left].isalnum():
                    left+=1
            if s[right].lower()!=s[left].lower():
                return False
            right-=1
            left+=1
        return True