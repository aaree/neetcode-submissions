class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        temp={}
        for string in strs:
            t=[0]*26
            for i in string:
                t[ord(i)-ord('a')]+=1
            if tuple(t) not in temp:
                temp[tuple(t)]=[]
            temp[tuple(t)].append(string)
        for key, val in temp.items():
            ans.append(val)
        return ans