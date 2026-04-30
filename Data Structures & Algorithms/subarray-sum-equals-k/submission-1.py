class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        temp={0:1}
        cnt=0
        t=[]
        for i in nums:
            if len(t)==0:
                t.append(i)
            else:
                t.append(i+t[-1])
        for i in t:
            opposite =i-k
            if opposite in temp:
                cnt+=temp[opposite]
            temp[i]=temp.get(i,0)+1
        return cnt