# Implement a trie with insert, search, and startsWith methods.

# Example:
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");
# trie.search("app");     // returns true

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.endhere = False

class Trie:
    def __init__(self):
        self.root = TreeNode(None)

    def insert(self, word):
        parent = self.root
        for i, char in enumerate(word):
            if char not in parent.children:
                parent.children[char] = TreeNode(char)
            parent = parent.children[char]
            if i == len(word)-1:
                parent.endhere = True

    def search(self, word):
        parent = self.root
        for char in word:
            if char not in parent.children:
                return False
            parent = parent.children[char]
        return parent.endhere

    def startsWith(self, prefix):
        parent = self.root
        for char in prefix:
            if char not in parent.children:
                return False
            parent = parent.children[char]
        return True
