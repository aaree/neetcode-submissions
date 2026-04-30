class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l=r=0
        arrSum=0
        cnt=0
        while r<len(arr):
            arrSum+=arr[r]
            while r-l+1>k:
                arrSum-=arr[l]
                l+=1
            if r-l+1==k:
                if arrSum/k>=threshold:
                    cnt+=1
            r+=1
        return cnt