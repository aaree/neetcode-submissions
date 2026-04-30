class Solution:
    def validPalindrome(self, s: str) -> bool:
        def pal(s):
            l=0
            r=len(s)-1
            while r>l:
                if s[r]!=s[l]:
                    return False
                r-=1
                l+=1
            return True
        delete=1
        left=0
        right=len(s)-1
        answer=True
        while right>left:
            if delete==1 and s[left]!=s[right]:
                delete-=1
                answer=pal(s[left+1:right+1]) or pal(s[left:right])
            left+=1
            right-=1
        return answer