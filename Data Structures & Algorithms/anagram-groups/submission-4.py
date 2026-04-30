class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        sort={}
        for i in strs:
            str_sort=''.join(sorted(list(i)))
            if str_sort not in sort:
                sort[str_sort]=[]
            sort[str_sort].append(i)
        for key,val in sort.items():
            ans.append(val)
        return ans