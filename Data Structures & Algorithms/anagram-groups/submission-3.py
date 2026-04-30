class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans={}
        for i in strs:
            list_str=list(i)
            list_str.sort()
            new=''.join(list_str)
            if new not in ans:
                ans[new]=[]
            ans[new].append(i)
        ans2=[]
        for key,val in ans.items():
            ans2.append(val)
        return ans2