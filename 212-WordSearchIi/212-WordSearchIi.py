# Last Updated: 6/22/2026, 12:42:26 AM
class Trie:
    def __init__(self):
        self.children={}
        self.isWord=False
    def addWord(self,word):
        root=self
        for char in word:
            if char not in root.children:
                root.children[char]=Trie()
            root=root.children[char]
        root.isWord=True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=Trie()
        rows=len(board)
        cols=len(board[0])
        for word in words:
            root.addWord(word)
        res=[]
        def backtrack(i,j,word,node):
            if not 0<=i<rows or not 0<=j<cols or board[i][j] not in node.children:
                return False
            temp=board[i][j]
            board[i][j]=None
            node=node.children[temp]
            word+=temp
            if node.isWord:
                res.append(word) 
            backtrack(i+1,j,word,node)
            backtrack(i-1,j,word,node)
            backtrack(i,j+1,word,node)
            backtrack(i,j-1,word,node)
            board[i][j]=temp
        for i in range(rows):
            for j in range(cols):
                backtrack(i,j,"",root)
        return list(set(res))
        