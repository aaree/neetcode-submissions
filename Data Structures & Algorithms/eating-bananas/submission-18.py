class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)

        while r>l:
            m=(r+l)//2
            hr=0
            for pile in piles:
                hr+=math.ceil(pile/m)
            if hr>h:
                l=m+1
            else:
                r=m
        return l