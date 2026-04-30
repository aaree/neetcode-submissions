class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxSpeed=0
        for i in piles:
            maxSpeed=max(maxSpeed,i)
        l=1
        r=maxSpeed
        while r>l:
            time=0
            m=(r+l)//2
            for i in piles:
                time+=math.ceil(i/m)
            print(time)
            if time>h:
                l=m+1
                print(r,l)
            else:
                r=m
                print(r,l)
        return l
            