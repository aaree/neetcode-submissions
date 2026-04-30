class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        while r>l:
            mid=0
            m=(r+l)//2
            for i in piles:
                mid+=math.ceil(i/m)
            if mid>h:
                l=m+1
            else:
                r=m
        return l