class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars)==1:
            return 1
        l=0
        r=0
        cnt=0
        while r<len(chars):
            cnt+=1
            if r==len(chars)-1 or chars[r]!=chars[r+1]:
                r+=1
                l+=1
                if cnt>1:
                    for i in str(cnt):
                        chars[l]=i
                        l+=1
                cnt=0
                if l<len(chars) and r<len(chars):
                    chars[l]=chars[r]
            else:
                r+=1
        print(cnt)
        while len(chars)>=l+1:
            chars.pop()
        print(l+1)
        return l+1