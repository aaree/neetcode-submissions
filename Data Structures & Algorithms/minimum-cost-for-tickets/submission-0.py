class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo={}
        def dfs(day):
            if day>=len(days):
                return 0
            if day in memo:
                return memo[day]
            one=costs[0]+dfs(day+1)
            nextVal=days[day]+7
            i=day
            while i<=len(days)-1 and nextVal>days[i]:
                i+=1
            seven=costs[1]+dfs(i)
            nextVal=days[day]+30
            i=day
            while i<=len(days)-1 and nextVal>days[i]:
                i+=1
            thirty=costs[2]+dfs(i)
            memo[day]=min(one,seven,thirty)
            return memo[day]
        
        return dfs(0)