class Solution:
    def confusingNumber(self, n: int) -> bool:
        invalid=set(['2','3','4','5','7'])
        valid={'0':'0','1':'1','6':'9','8':'8','9':'6'}
        new=''
        for i in str(n):
            if i in invalid:
                return False
            new+=valid[i]
        new=new[::-1]
        return not new==str(n)