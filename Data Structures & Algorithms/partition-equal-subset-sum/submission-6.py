class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2==1:
            return False
        target=sum(nums)/2
        ans=set()
        for i in nums:
            next=set()
            for j in ans:
                val=j+i
                if val==target:
                    return True
                if val not in ans:
                    next.add(val)
            ans.update(next)
            if i not in ans:
                if i==target:
                    return True
                ans.add(i)
        for i in ans:
            if i==target:
                return True
        return False
        
                
