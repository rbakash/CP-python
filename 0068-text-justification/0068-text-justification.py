class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def getAllWords(startingIndex)->list[str]:
            currentLength=0
            currentWords=[]
            while startingIndex < len(words) and currentLength +len(words[startingIndex]) <=maxWidth:
                currentWords.append(words[startingIndex])
                currentLength += len(words[startingIndex])+1
                startingIndex+=1
            return currentWords
        
        def createLine(currentLine,index):
            # Calculate the currentLength of all words
            currentLength = -1
            for eachWord in currentLine:
                currentLength += len(eachWord)+1

            if len(currentLine) ==1 or index == len(words):
                return " ".join(currentLine) + " " * (maxWidth - currentLength)
            wordCount = len(currentLine)-1
            spacesNeededPerWord = (maxWidth - currentLength) // wordCount
            extraSpaceAfterEachWord = (maxWidth - currentLength) % wordCount

            # Assign the extra Space from the left
            for spaceIndex in range(extraSpaceAfterEachWord):
                currentLine[spaceIndex]+=" "

            # Assign space Per word
            for spaceIndex in range(wordCount):
                currentLine[spaceIndex]+= " "*spacesNeededPerWord
            
            # Concatinate the words to form a line
            return " ".join(currentLine)
        
        # results=[]
        # index = 0
        
        # while index < len(words):
        #     currentLine=getAllWords(index)
        #     index+=len(currentLine)
        #     results.append(createLine(currentLine,index))

        results, currentLength, currentWords = [],0,[]
        for eachWord in words:
            if currentLength + len(currentWords) + len(eachWord) > maxWidth:
                if len(currentWords) ==1:
                    
                    results.append(currentWords[0] + ' ' * (maxWidth - currentLength))
                else:
                    spacesNeeded = maxWidth - (currentLength)
                    spacesNeededPerWord,extraSpaceAfterEachWord = divmod( spacesNeeded, len(currentWords)-1)

                    for spaceIndex in range(extraSpaceAfterEachWord):
                        currentWords[spaceIndex]+=" "
                    results.append((" "*spacesNeededPerWord).join(currentWords))
                currentWords,currentLength = [],0
            currentWords+=[eachWord]
            currentLength += len(eachWord)
        print(currentWords, currentLength)
        finalLine = ' '.join(currentWords)
        results.append(finalLine + ' ' * (maxWidth - len(finalLine)))
       
        return results