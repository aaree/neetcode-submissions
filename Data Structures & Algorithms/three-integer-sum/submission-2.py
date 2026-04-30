class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(arr,i):
            a=0
            b=len(arr)-1
            target=0-arr[i]
            all=set()
            while a<b:
                if a==i:
                    a+=1
                    continue
                if b==i:
                    b-=1
                    continue
                total=arr[a]+arr[b]
                if total>target:
                    b-=1
                elif total<target:
                    a+=1
                else:
                    if a!=b:
                        all.add(tuple(sorted((arr[i],arr[a],arr[b]))))
                        a+=1
            return all

        nums.sort()
        ans=set()
        for i in range(len(nums)):
            final=twoSum(nums,i)
            if final is not None and final not in ans:
                ans.update(final)
        print(ans)
        ans2=[]
        for i in ans:
            ans2.append(list(i))
        return ans2