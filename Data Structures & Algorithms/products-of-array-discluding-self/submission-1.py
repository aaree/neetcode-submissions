class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new=[1]
        for i in nums:
            new.append(new[-1]*i)
        new.pop()
        reverse=[1]
        nums.reverse()
        for i in nums:
            reverse.append(reverse[-1]*i)
        reverse.pop()
        reverse.reverse()
        final=[]
        print(reverse)
        i=0
        while i<len(nums):
            total=new[i]*reverse[i]
            final.append(total)
            i+=1
        return final