class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        while r>l:
            time=0
            m=(r+l)//2
            for i in piles:
                time+=math.ceil(i/m)
            if time>h:
                l=m+1
            else:
                r=m
        return l