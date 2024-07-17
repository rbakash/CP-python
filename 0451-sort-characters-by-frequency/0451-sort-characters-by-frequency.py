class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = defaultdict(int)
        maxFrequency = 0
        for eachCharacter in s:
            frequency[eachCharacter] += 1
            maxFrequency = max(maxFrequency, frequency[eachCharacter])

        buckets = [[] for _ in range(maxFrequency + 1)]

        for character, count in frequency.items():
            buckets[count].append(character)

        string = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        result = ""
        for index in range(len(buckets) - 1, 0, -1):
            for eachCharacter in buckets[index]:
                result += eachCharacter * index
        return result
