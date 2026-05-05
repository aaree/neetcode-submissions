class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=''
        for i in range(len(strs[0])):
            temp=prefix
            prefix+=strs[0][i]
            for str in strs:
                if not str.startswith(prefix) or len(str)<=i:
                    return temp
        return prefix

        
