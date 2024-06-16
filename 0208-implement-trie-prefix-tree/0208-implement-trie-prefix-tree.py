class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfWord=False
class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        current = self.root

        for eachCharacter in word:
            if eachCharacter not in current.children:
                current.children[eachCharacter] = TrieNode()
            current = current.children[eachCharacter]
        current.endOfWord = True
        
    def search(self, word: str) -> bool:
        current = self.root
        for eachCharacter in word:
            if eachCharacter not in current.children:
                return False
            current = current.children[eachCharacter]
        return current.endOfWord

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for eachCharacter in prefix:
            if eachCharacter not in current.children:
                return False
            current = current.children[eachCharacter]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)