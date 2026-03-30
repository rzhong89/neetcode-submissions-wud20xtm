class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        
        for w in words:
            root.addWord(w)

        res = set()
        visited = set()

        def dfs(r, c, node, word):
            if min(r, c) < 0 or r >= len(board) or c >= len(board[0]) or (r, c) in visited or board[r][c] not in node.children:
                return
            
            visited.add((r, c))

            node = node.children[board[r][c]]
            word += board[r][c]
            
            if node.isWord == True:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            
            visited.remove((r, c))

        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, root, "")

        return list(res)