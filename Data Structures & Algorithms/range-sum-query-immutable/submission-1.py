class NumArray:

    def __init__(self, nums: List[int]):
        self.arr=[0]
        total=0
        for i in nums:
            total+=i
            self.arr.append(total)

    def sumRange(self, left: int, right: int) -> int:
        return self.arr[right+1]-self.arr[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)