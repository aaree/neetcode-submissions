class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d={}
        l=r=0
        maxW=0
        while r<len(fruits):
            right=fruits[r]
            d[right]=d.get(right,0)+1
            while len(d)>2:
                d[fruits[l]]-=1
                if d[fruits[l]]==0:
                    del d[fruits[l]]
                l+=1
            w=r-l+1
            maxW=max(maxW,w)
            r+=1
        return maxW