class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouping={}
        answer=[]
        for word in strs:
            key=[0]*26
            print(key)
            for i in word:
                key[ord(i)-ord('a')]+=1
            key=tuple(key)
            if key not in grouping:
                grouping[key]=[]
            grouping[key].append(word)
        for key, val in grouping.items():
            answer.append(val)
        return answer