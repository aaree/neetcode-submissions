class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        parent={}
        rank={}
        adj={}

        for a,b in synonyms:
            if a not in adj:
                adj[a]=[]
            if b not in adj:
                adj[b]=[]
            adj[a].append(b)
            adj[b].append(a)
        
        for key, val in adj.items():
            parent[key]=key
            rank[key]=1

        def find(n):
            while n!=parent[n]:
                parent[n]=parent[parent[n]]
                n=parent[n]
            return parent[n]
        
        def union(n1,n2):
            a,b=find(n1),find(n2)
            if a==b:
                return False
            if rank[a]>rank[b]:
                parent[b]=a
                rank[a]+=rank[b]
            else:
                parent[a]=b
                rank[b]+=rank[a]
            return True
        for a,b in synonyms:
            union(a,b)
        seen=set()
        temp=[]
        def dfs(pointer,arr):
            if pointer>=len(arr):
                if tuple(arr.copy()) not in seen:
                    seen.add(tuple(arr.copy()))
                    temp.append(arr.copy())
                    return
                else:
                    return
            dfs(pointer+1,arr)
            if arr[pointer] in parent:
                word=arr[pointer]
                for w in parent:
                    if find(word)==find(w):
                        arr[pointer]=w
                        dfs(pointer+1,arr)
                        arr[pointer]=word
        textArr=text.split(' ')
        dfs(0,textArr)
        final=[]
        for arr in temp:
            final.append(' '.join(arr))
        return sorted(final)