class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks)%4!=0:
            return False
        ans=[0,0,0,0]
        matchsticks.sort(key=lambda x: -x)
        def dfs(arr,pointer):
            if (pointer==len(matchsticks)) and (arr[0]==arr[1]==arr[2]==arr[3]):
                return True
            elif pointer==len(matchsticks):
                print(arr)
                return
            val=matchsticks[pointer]
            for j in range(len(arr)):
                if arr[j]+val<=sum(matchsticks)//4:
                    arr[j]+=val
                    if dfs(arr,pointer+1):
                        return True
                    arr[j]-=val
        
        if dfs(ans,0):
            return True
        else:
            return False