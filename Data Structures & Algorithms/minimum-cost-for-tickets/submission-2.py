class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo={}
        def dfs(pointer):
            if pointer>=len(days):
                return 0
            if pointer in memo:
                return memo[pointer]
            pointerDummy=pointer
            res=0
            res1=dfs(pointer+1)+costs[0]
            day2=days[pointer]+7
            while pointerDummy<len(days) and day2>days[pointerDummy]:
                pointerDummy+=1
            res2=dfs(pointerDummy)+costs[1]
            pointerDummy=pointer
            day3=days[pointer]+30
            while pointerDummy<len(days) and day3>days[pointerDummy]:
                pointerDummy+=1
            res3=costs[2]+dfs(pointerDummy)
            memo[(pointer)]= min(res1,res2,res3)
            return memo[pointer]
        return dfs(0)