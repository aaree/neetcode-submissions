class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=""
        max_prefix=""
        for i in strs[0]:
            prefix+=i
            match=True
            for j in strs:
                if not j.startswith(prefix):
                    match=False
            if match==False:
                break
            max_prefix=prefix
        return max_prefix