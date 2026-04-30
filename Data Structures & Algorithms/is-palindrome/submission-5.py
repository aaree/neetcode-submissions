import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        test=[i.lower().strip(string.punctuation) for i in s.split()]
        t=''.join(test)
        t2=[]
        for i in t:
            if i not in string.punctuation:
                t2.append(i)
        t=''.join(t2)
        a=0
        b=len(t)-1        
        while a<b:
            if t[a]!=t[b]:
                return False
            a+=1
            b-=1
        return True