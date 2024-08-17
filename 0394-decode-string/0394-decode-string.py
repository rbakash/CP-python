class Solution:
    index = 0
    def decodeStringEditorial(self, s: str) -> str:
        
        result=[]
        while self.index<len(s) and s[self.index]!=']':
            print(s[self.index].isdigit())
            if not s[self.index].isdigit():
                result.append(s[self.index])
                self.index+=1
            else:
                times = 0
                while self.index<len(s) and s[self.index].isdigit():
                    times = times *10 + int(s[self.index])
                    self.index+=1
                self.index+=1
                decodedString= self.decodeString(s)
                self.index+=1
                result.append(decodedString*times)
        return "".join(result)

    def decodeString(self, s: str) -> str:    
        stack,currentString,currentNum=[],"",0
        for char in s:
            # start on new endcoding
            if char == "[":
                stack.append(currentString)
                stack.append(currentNum)
                currentString=""
                currentNum =0
            elif char == "]":
                # Perform the decoding
                prevNum = stack.pop()
                prevString = stack.pop()
                currentString = prevString + prevNum * currentString
            elif char.isdigit():
                currentNum = currentNum*10 + int(char)
            else:
                currentString += char
        return currentString