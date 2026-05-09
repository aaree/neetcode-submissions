class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[0]*len(nums1)
        temp={}
        stack=[]
        for i, num in enumerate(nums2):
            if len(stack)==0:
                stack.append((i,num))
            else:
                if stack[-1][1]>num:
                    stack.append((i,num))
                else:
                    while stack and num>stack[-1][1]:
                        i2,num2=stack.pop()
                        temp[num2]=num
                    stack.append((i,num))
        for i, num in enumerate(nums1):
            if num in temp:
                ans[i]=temp[num]
            else:
                ans[i] = -1
        return ans
        