class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ans=False
        memo={}
        def backtrack(word):
            nonlocal ans
            if word in memo: return memo[word]
            if len(word)==0:
                ans=True
                return True
            for i in wordDict:
                if word.startswith(i):
                    if backtrack(word[len(i):]):
                        memo[word] = True
                        return True
            memo[word] = False
            return False
        backtrack(s)
        return ans