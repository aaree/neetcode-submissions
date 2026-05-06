class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        Letters=set()
        for word in words:
            for l in list(word):
                Letters.add(l)
        adj={}
        for l in Letters:
            adj[l]=[]
        for i in range(1,len(words)):
            word1=words[i-1]
            word2=words[i]
            if word1.startswith(word2) and len(word1)>len(word2):
                return ''
            for i in range(min(len(word1),len(word2))):
                if word1[i]!=word2[i]:
                    adj[word1[i]].append(word2[i])
                    break
        loop=set()
        seen=set()
        answer=[]
        def dfs(letter):
            if letter in loop:
                return False
            if letter in seen:
                return True
            loop.add(letter)
            if letter in adj:
                for l in adj[letter]:
                    if not dfs(l):
                        return False
            loop.remove(letter)
            seen.add(letter)
            answer.append(letter)
            return True
        for l in Letters:
            if not dfs(l):
                return ''
        answer.reverse()
        return ''.join(answer)
