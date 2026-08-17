class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp={}
        for st in strs:
            arr=[0]*26
            for i in st:
                num=ord(i)-ord('a')
                arr[num]+=1
            arr=tuple(arr)
            if arr in temp:
                temp[arr].append(st)
            else:
                temp[arr]=[]
                temp[arr].append(st)
        ans=[]
        for key, val in temp.items():
            ans.append(list(val))
        return ans