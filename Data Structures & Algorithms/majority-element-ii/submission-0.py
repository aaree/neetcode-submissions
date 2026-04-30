class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic={}
        limit=len(nums)/3
        print(limit)
        ans=set()
        for i,val in enumerate(nums):
            dic[val]=dic.get(val,0)+1
            if dic[val]>limit:
                ans.add(val)
        print(dic)
        return list(ans)