class Trie:
    """
    Implement a trie with insert, search, and startsWith methods.
    """
    def __init__(self):
        # A standard dictionary works perfectly here
        self.root = {}

    def insert(self, word: str) -> None:
        """Inserts a word into the trie."""
        current = self.root
        for letter in word:
            current = current.setdefault(letter, {})
        current["_end"] = True

    def search(self, word: str) -> bool:
        """Returns if the word is in the trie."""
        current = self.root
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
        return "_end" in current

    def startsWith(self, prefix: str) -> bool:
        """Returns if there is any word in the trie that starts with the given prefix."""
        current = self.root
        for letter in prefix:
            if letter not in current:
                return False
            current = current[letter]
        return True


# Testing the class (Updated with Python 3 print functions)
test = Trie()
test.insert('helloworld')
test.insert('ilikeapple')
test.insert('helloz')

print(test.search('hello'))       # Output: False
print(test.startsWith('hello'))   # Output: True
print(test.search('ilikeapple'))  # Output: True