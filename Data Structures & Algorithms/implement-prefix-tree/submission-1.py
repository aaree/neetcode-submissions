class PrefixNode:
    def __init__(self):
        self.children={}
        self.word=False

class PrefixTree:

    def __init__(self):
        self.root=PrefixNode()

    def insert(self, word: str) -> None:
        curr=self.root
        for w in word:
            if w not in curr.children:
                curr.children[w]=PrefixNode()
                curr=curr.children[w]
            else:
                curr=curr.children[w]
        curr.word=True

    def search(self, word: str) -> bool:
        curr=self.root
        for w in word:
            if w not in curr.children:
                return False
            else:
                curr=curr.children[w]
        return curr.word

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for w in prefix:
            if w not in curr.children:
                return False
            else:
                curr=curr.children[w]
        return True
        
        