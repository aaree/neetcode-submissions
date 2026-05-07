class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target=sum(stones)/2
        total=set()
        for stone in stones:
            temp=set()
            for val in total:
                val+=stone
                temp.add(val)
            total.add(stone)
            total.update(temp)
        minWeight=math.inf
        for stone in total:
            remainder=abs(target-stone)*2
            minWeight=min(remainder,minWeight)
        return int(minWeight)