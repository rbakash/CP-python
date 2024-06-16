class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfWord=False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for eachCharacter in word:
            if eachCharacter not in current.children:
                current.children[eachCharacter]=TrieNode()
            current = current.children[eachCharacter]
        current.endOfWord = True

    def search(self, word: str) -> bool:
        
        def searchInAllNode(subString, node)-> bool:

            for index,each in enumerate(subString):
               
                if each not in node.children:  
                    if each ==".":
                        for eachChildren in node.children.values():
            
                            if  searchInAllNode(subString[index+1:],eachChildren):
                                return True
                    return False
                            
                else:
                    node = node.children[each]
            return node.endOfWord
        return searchInAllNode(word,self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)