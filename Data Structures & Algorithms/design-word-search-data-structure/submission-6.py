class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c]
        
        curr.isWord = True

    def search(self, word: str) -> bool:
        def dfs(i, root):
            curr = root

            for j in range(i, len(word)):
                if word[j] == ".":
                    # search all directions
                    for child in curr.children.values():
                        if dfs(j + 1, child):
                            return True
                    return False
                elif word[j] in curr.children:
                    curr = curr.children[word[j]]
                else:
                    return False
                
            return curr.isWord

        return dfs(0, self.root)
