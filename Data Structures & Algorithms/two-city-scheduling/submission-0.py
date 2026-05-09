class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        memo={}
        def dfs(a,b,pointer):
            if pointer==len(costs):
                return 0
            if (a,b,pointer) in memo:
                return memo[(a,b,pointer)]
            a1=math.inf
            b1=math.inf
            if a>0:
                a1=costs[pointer][0]+dfs(a-1,b,pointer+1)
            if b>0:
                b1=costs[pointer][1]+dfs(a,b-1,pointer+1)
            memo[(a,b,pointer)]= min(a1,b1)
            return memo[(a,b,pointer)]
        return dfs(len(costs)/2,len(costs)/2,0)                