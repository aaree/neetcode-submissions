class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        unique_values = set(s)
        max_window=0
        for i in unique_values:
            left=0
            right=0
            replace=k
            while right<len(s):
                if i!=s[right]:
                    replace-=1
                while replace<0:
                    if s[left]!=i:
                        replace+=1
                    left+=1
                window=right-left+1
                max_window=max(max_window,window)
                right+=1
        return max_window



        