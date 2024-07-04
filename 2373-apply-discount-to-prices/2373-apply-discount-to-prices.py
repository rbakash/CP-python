class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        discount = discount / 100
        words = sentence.split(" ")
        for index, eachWord in enumerate(words):
            if eachWord[0] == "$":
                eachWord = eachWord[1:]
                if eachWord.isdigit():
                    newPrice = int(eachWord) - (int(eachWord) * discount)
                    eachWord = "$" + "{:.2f}".format(newPrice)
                    words[index] = eachWord
        return " ".join(words)
