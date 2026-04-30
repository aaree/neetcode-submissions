class Solution:
    def partition(self, s: str) -> List[List[str]]:
        final=[]
        def is_palindrome(s):
            l=0
            r=len(s)-1
            while r>l:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        def backtrack(s,arr):
            if len(s)==0:
                final.append(arr.copy())
            for endPointer in range(1,len(s)+1):
                if is_palindrome(s[:endPointer]):
                    arr.append(s[:endPointer])
                    backtrack(s[endPointer:],arr)
                    arr.pop()
        
        backtrack(s,[])
        return final