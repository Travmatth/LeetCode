"""
Implement a trie with insert, search, and startsWith methods.
Note:
You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""

class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        root = self.trie
        for c in word:
            if c not in root:
                root[c] = {}
            root = root[c]
        root[0] = True


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        root = self.trie
        for c in word:
            if c in root:
                root = root[c]
            else:
                return False
        return True if 0 in root else False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        root = self.trie
        for c in prefix:
            if c not in root:
                return False
            root = root[c]
        return True

if __name__ == "__main__":
    trie = Trie();
    trie.insert("apple");
    ex_0 = trie.search("apple");   # returns true
    ex_1 = trie.search("app");     # returns false
    ex_2 = trie.startsWith("app"); # returns true
    trie.insert("app");   
    ex_3 = trie.search("app");     # returns true
    pass