class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue=deque()
        heap=[]
        r=0
        t={}
        while r<k:
            queue.append(nums[r])
            heapq.heappush(heap,-nums[r])
            t[nums[r]]=t.get(nums[r],0)+1
            r+=1
        ans=[]
        while r<len(nums):
            ans.append(-heap[0])
            val=queue.popleft()
            t[val]-=1
            queue.append(nums[r])
            heapq.heappush(heap,-nums[r])
            t[nums[r]]=t.get(nums[r],0)+1
            while heap and t.get(-heap[0], 0) == 0:
                heapq.heappop(heap)
            r+=1
        ans.append(-heap[0])
        return ans