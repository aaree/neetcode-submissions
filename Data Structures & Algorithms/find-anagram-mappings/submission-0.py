class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        seen=set()
        for i,val1 in enumerate(nums1):
            for j, val2 in enumerate(nums2):
                if val1==val2 and j not in seen:
                    seen.add(j)
                    ans.append(j)
                    break
        return ans