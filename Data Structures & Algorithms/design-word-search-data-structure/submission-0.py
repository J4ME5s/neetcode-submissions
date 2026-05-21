class WordDictionary:

    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def addWord(self, word: str) -> None:
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = WordDictionary()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        return self.dfs(word, 0, self)
    
    def dfs(self, word: str, index: int, node: WordDictionary) -> bool:
        if index == len(word):
            return node.endOfWord
        
        c = word[index]
        if c == '.':
            for child in node.children.values():
                if self.dfs(word, index + 1, child):
                    return True
            return False
        
        if c not in node.children:
            return False
        
        return self.dfs(word, index + 1, node.children[c])

