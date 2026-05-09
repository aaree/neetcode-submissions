class Solution:
    def customSortString(self, order: str, s: str) -> str:
        adj={}
        for i in range(1,len(order)):
            if order[i-1]!=order[i]:
                adj[order[i-1]]=order[i]
        loop=set()
        seen=set()
        ans=[]
        def dfs(l):
            if l in loop:
                return False
            if l in seen:
                return True
            loop.add(l)
            if l in adj:
                for let in adj[l]:
                    if not dfs(let):
                        return False
            loop.remove(l)
            seen.add(l)
            ans.append(l)
            return True
        for i in order:
            dfs(i)
        ans.reverse()
        final=[]
        c=Counter(s)
        sAll=set(list(s))
        for i in ans:
            if i in sAll:
                for _ in range(c[i]):
                    final.append(i)
        for j in sAll:
            if j not in order:
                for _ in range(c[j]):
                    final.append(j)
        return ''.join(final)
