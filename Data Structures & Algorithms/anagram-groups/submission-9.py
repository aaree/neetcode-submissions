class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        m={}
        for s in strs:
            count=[0]*26
            for i in s:
                count[ord(i)-ord('a')]+=1
            if tuple(count) not in m:
                m[tuple(count)]=[]
            m[tuple(count)].append(s)
        for key, value in m.items():
            ans.append(value)
        return ans