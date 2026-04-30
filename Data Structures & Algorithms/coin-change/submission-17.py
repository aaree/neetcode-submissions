class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        total=set()
        seen=set()
        big=True
        for i in coins:
            if i<=amount:
                big=False
            if i==amount:
                return 1
            total.add((i,1))
        if big:
            return -1
        while True:
            temp=set()
            tooBig=True
            for val, num in total:
                for i in coins:
                    newVal=val+i
                    newNum=num+1
                    if newVal in seen:
                        continue
                    if newVal>amount:
                        continue
                    if newVal==amount:
                        return newNum
                    if newVal<=amount:
                        tooBig=False
                    temp.add((newVal,newNum))
                    seen.add(newVal)
            if tooBig:
                return -1
            total.update(temp)

