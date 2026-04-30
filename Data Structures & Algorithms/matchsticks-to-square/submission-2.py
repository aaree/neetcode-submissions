class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks)%4!=0:
            return False
        ans=[0,0,0,0]
        matchsticks.sort(key=lambda x: -x)
        equalSides=None
        def dfs(arr,pointer):
            nonlocal equalSides
            if equalSides:
                return
            if (pointer==len(matchsticks)) and (arr[0]==arr[1]==arr[2]==arr[3]):
                #print(arr)                
                equalSides=True
                return
            elif pointer==len(matchsticks):
                print(arr)
                return
            val=matchsticks[pointer]
            for j in range(len(arr)):
                if arr[j]+val<=sum(matchsticks)//4:
                    arr[j]+=val
                    dfs(arr,pointer+1)
                    arr[j]-=val
        dfs(ans,0)
        if equalSides:
            return True
        else:
            return False