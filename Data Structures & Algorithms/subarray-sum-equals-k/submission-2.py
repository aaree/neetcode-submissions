class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        arr={0:1}
        cnt=0
        total=0
        for i, val in enumerate(nums):
            total+=val
            opposite=total-k
            if opposite in arr:
                cnt+=arr[opposite]
            arr[total]=arr.get(total,0)+1
        return cnt 