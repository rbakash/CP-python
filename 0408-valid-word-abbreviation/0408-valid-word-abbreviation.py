class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        wordIterator,abbrIterator, length =0,0,0
        n = len(word)
        while abbrIterator < len(abbr) and wordIterator < len(word):
            if abbr[abbrIterator].isdigit():
                if abbr[abbrIterator] =='0':
                    return False
                # Traverse till a char is found to get the length
                index = abbrIterator
                print(abbrIterator)
                while index < len(abbr) and abbr[index].isdigit():
                    index+=1
                length = int(abbr[abbrIterator:index])
                print(length)
                wordIterator += length
                abbrIterator =index
                print(abbrIterator)
                # print(word[wordIterator],abbr[abbrIterator])
            else:
                if word[wordIterator] != abbr[abbrIterator]:
                    return False
                wordIterator+=1
                abbrIterator+=1
        
        return wordIterator == len(word) and  abbrIterator == len(abbr)

                 
                
