class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        total=set()
        big=True
        for i in coins:
            if i<=amount:
                big=False
            if i==amount:
                return 1
            total.add((i,1))
        if big:
            return -1
        print(total)
        while True:
            temp=set()
            for val, num in total:
                tooBig=True
                for i in coins:
                    newVal=val+i
                    newNum=num+1
                    if newVal==amount:
                        return newNum
                    if newVal<=amount:
                        tooBig=False
                    temp.add((newVal,newNum))
            if tooBig:
                return -1
            total.update(temp)

