class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        total=deque()
        seen=set()
        big=True
        for i in coins:
            if i<=amount:
                big=False
            if i==amount:
                return 1
            total.append((i,1))
        if big:
            return -1
        while total:
            temp=set()
            for i in range(len(total)):
                val, num = total.popleft()
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
                    total.append((newVal,newNum))
                    seen.add(newVal)
        return -1        

