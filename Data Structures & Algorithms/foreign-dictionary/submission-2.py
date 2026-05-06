class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        letters=set()
        ans=[]
        adj={}
        for word in words:
            l=list(word)
            for w in l:
                letters.add(w)
        for letter in letters:
            adj[letter]=[]
        for i in range(1,len(words)):
            word1=words[i-1]
            word2=words[i]
            while word1.startswith(word2):
                if len(word1)>len(word2):
                    return ''
                elif word1==word2:
                    break
            for i in range(min(len(word1),len(word2))):
                if word1[i]!=word2[i]:
                    adj[word1[i]].append(word2[i])
                    break
        loop=set()
        seen=set()
        order=[]
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
            order.append(letter)
            return True
        for l in letters:
            if not dfs(l):
                return ''
        order.reverse()
        return ''.join(order)
        
        
