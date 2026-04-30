class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c=Counter(tasks)
        temp=[]
        maxVal=0
        for key, val in c.items():
            if val>maxVal:
                maxVal=val
                maxKey=key
        del c[maxKey]
        skip=(maxVal-1)*n
        other=0
        carry=0
        for key, val in c.items():
            skip-=min(maxVal-1,val)        
        return max(0,skip)+len(tasks)


        