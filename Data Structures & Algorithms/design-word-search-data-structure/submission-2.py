class trieNode:
    def __init__(self):
        self.children={}
        self.word=False

class WordDictionary:

    def __init__(self):
        self.root=trieNode()

    def addWord(self, word: str) -> None:
        curr=self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=trieNode()
            curr=curr.children[c]
        curr.word=True

    def dfs(self,node,word):
        if len(word)==0:
            return node.word
        if word[0]=='.':
            for i in node.children:
                if self.dfs(node.children[i],word[1:]):
                    return True
            return False
        else:
            if word[0] not in node.children:
                return False
            return self.dfs(node.children[word[0]],word[1:])

    
    def search(self, word: str) -> bool:
        curr=self.root
        return self.dfs(curr,word)
