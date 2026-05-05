class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        temp={}
        for str in strs:
            key=[0]*26
            for i in str:
                val=ord(i)-ord('a')
                key[val]+=1
            if tuple(key) not in temp:
                temp[tuple(key)]=[]
            temp[tuple(key)].append(str)
        for key, val in temp.items():
            ans.append(val)
        return ans