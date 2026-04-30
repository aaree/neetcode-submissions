class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans={}
        for s in strs:
            temp=[0]*27
            for i in s:
                num=ord(i)-ord('a')+1
                temp[num]+=1
            if tuple(temp) not in ans:
                ans[tuple(temp)]=[]
            ans[tuple(temp)].append(s)
        final=[]
        for key, val in ans.items():
            final.append(val)
        return final