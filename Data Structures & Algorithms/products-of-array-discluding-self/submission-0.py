class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref=[]
        for i in nums:
            if len(pref)==0:
                pref.append(i)
            else:
                pref.append(pref[-1]*i)
        suff=[]
        nums.reverse()
        for j in nums:
            if len(suff)==0:
                suff.append(i)
            else:
                suff.append(suff[-1]*j)
        print(pref)
        print(suff)
        total=[]
        suff.reverse()
        for i in range(len(nums)):
            if i==0:
                total.append(suff[1])
            elif i==len(nums)-1:
                total.append(pref[-2])
            else:
                total.append(suff[i+1]*pref[i-1])
        return total