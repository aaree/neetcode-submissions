class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        ans=set()
        seen=set()
        for i in coins:
            if i==amount:
                return 1
            ans.add((1,i))
        total=0
        cnt=0
        seen=set()
        while len(ans)>0:
            set2=set()
            a=[]
            for num,coin in ans:
                for i in coins:
                    if coin+i<amount and (coin+i) not in seen:
                        set2.add((num+1,coin+i))
                        seen.add(coin+i)
                    elif coin+i==amount:
                        return num+1
                ans=set2
        return -1
        
