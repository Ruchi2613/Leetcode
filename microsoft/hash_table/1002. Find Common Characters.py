import collections


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        word_size = len(words)
        res = []

        common_character_counts = collections.Counter(words[0])

        for i in range(1, word_size):
            current_character_counts = collections.Counter(words[i])


            for letter in common_character_counts.keys():
                common_character_counts[letter] = min(common_character_counts[letter],              current_character_counts[letter])


        for letter, count in common_character_counts.items():
            for c in range(count):
                res.append(letter)

        return res



                
 
        

"""

e:1
l:2

"""


"""
res = {
c:1,
o:1
}


word = cook

c:1
o:2
k:1
"""