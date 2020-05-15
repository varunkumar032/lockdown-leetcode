from solutions.day14_ImplementTrie import TreeNode, Trie

# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");
# trie.search("app");     // returns true

def test_day14_01():
    trie = Trie()
    trie.insert("apple")
    a = trie.search("apple")
    b = trie.search("app")
    c = trie.startsWith("app")
    trie.insert("app")
    d = trie.search("app")
    assert (a, b, c, d) == (True, False, True, True)

def test_day14_02():
    trie = Trie()
    trie.insert("apple")
    a = trie.search("mango")
    b = trie.search("appleapple")
    trie.insert("mango")
    c = trie.search("mango")
    d = trie.startsWith("man")
    assert (a, b, c, d) == (False, False, True, True)
