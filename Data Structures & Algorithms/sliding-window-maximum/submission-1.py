class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxVal=-math.inf
        dic={}
        queue=deque()
        r=0
        while r<k:
            queue.append(nums[r])
            r+=1
        ans=[]
        while r<len(nums):
            total=max(queue)
            ans.append(total)
            queue.popleft()
            queue.append(nums[r])
            r+=1
        ans.append(max(queue))
        return ans
