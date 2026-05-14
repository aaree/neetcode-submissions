class prefixNode:
    def __init__(self):
        self.word=False
        self.children={}

class PrefixTree:

    def __init__(self):
        self.root=prefixNode()

    def insert(self, word: str) -> None:
        node=self.root
        for w in word:
            if w not in node.children:
                node.children[w]=prefixNode()
            node=node.children[w]
        node.word=True

    def search(self, word: str) -> bool:
        node=self.root
        for w in word:
            if w not in node.children:
                return False
            node=node.children[w]
        return node.word

    def startsWith(self, prefix: str) -> bool:
        node=self.root
        for w in prefix:
            if w not in node.children:
                return False
            node=node.children[w]
        return True
        