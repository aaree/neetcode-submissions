class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]
        total=sum(stones)
        half=total//2
        capacity=len(stones)+1
        DP=set()
        for stone in stones:
            temp=set()
            newTotal=0
            for key in DP:
                #print(key)
                newTotal=key+stone
                if newTotal<=half:
                    temp.add(newTotal)
            if stone<=half:
                temp.add(stone)
            DP.update(temp)
            #print(temp)
        minval=math.inf
        final=None
        for key in DP:
            if total-2*key<minval:
                minval=total-2*key
        #print(DP)
        return minval