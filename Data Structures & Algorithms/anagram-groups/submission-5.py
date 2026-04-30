class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans={}
        final=[]
        for word in strs:
            temp=[0]*26
            for i in word:
                num=ord(i)-ord('a')
                temp[num]+=1
            t=tuple(temp)
            if t not in ans:
                ans[t]=[]
            ans[t].append(word)
        for key, val in ans.items():
            final.append(val)
        return final