class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        parent={}
        rank={}
        allVal=set(nums)
        for num in nums:
            parent[num]=num
            rank[num]=1
        def find(num):
            while num!=parent[num]:
                parent[num]=parent[parent[num]]
                num=parent[num]
            return parent[num]
        def union(num1,num2):
            a,b=find(num1),find(num2)
            if a==b:
                return False
            if rank[a]>rank[b]:
                parent[b]=a
                rank[a]+=rank[b]
            else:
                parent[a]=b
                rank[b]+=rank[a]
            return True
        for num in nums:
            if num-1 in allVal:
                union(num-1,num)
            if num+1 in allVal:
                union(num+1,num)
        return max(rank.values())