class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters={}
        longest_string=""
        left=0
        for right in range(len(s)):
            characters[s[right]]=characters.get(s[right],0)+1
            if characters[s[right]]>1:
                while characters[s[right]]>1:
                    characters[s[left]]=characters.get(s[left],0)-1
                    left+=1                    
            string=s[left:right+1]
            if len(string)>len(longest_string):
                longest_string=string
        print(longest_string)
        return len(longest_string)