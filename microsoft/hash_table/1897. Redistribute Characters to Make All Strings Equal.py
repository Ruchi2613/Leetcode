class Solution:
    def makeEqual(self, words) -> bool:
        
        d = {}

        for word in words:
            for letter in word:
                if letter not in d:
                    d[letter] = 1
                else:
                    d[letter]+=1

        n = len(words)

        for val in d.values():
            if val%n!= 0:
                return False

        return True