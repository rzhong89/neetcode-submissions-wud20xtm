class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root

        for c in word:
            if c in current.children:
                current = current.children[c]
            else:
                current.children[c] = TrieNode()
                current = current.children[c]

        current.endOfWord = True

    def search(self, word: str) -> bool:
        current = self.root

        for c in word:
            if c in current.children:
               current = current.children[c]
            else:
                return False

        return current.endOfWord

    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for c in prefix:
            if c in current.children:
               current = current.children[c]
            else:
                return False

        return True
        
        