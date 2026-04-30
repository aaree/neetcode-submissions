class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        currentVal=0
        currentLoc=0
        total=0
        for i in range(len(gas)):
            currentVal+=gas[i]-cost[i]
            total+=gas[i]-cost[i]
            if currentVal<0:
                currentLoc=i+1
                currentVal=0
                print(currentLoc)
        if total<0:
            return -1
        return currentLoc
