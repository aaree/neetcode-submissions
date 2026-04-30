class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rev=[1]
        pre=[1]
        start=1
        back=1
        final=[]
        for i in nums:
            start*=i
            pre.append(start)
        nums.reverse()
        for i in nums:
            back*=i
            rev.append(back)
        rev.reverse()
        print(rev)
        print(pre)
        for i in range(len(nums)):
            final.append(rev[i+1]*pre[i])
        return final