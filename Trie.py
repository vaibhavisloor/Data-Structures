class TrieNode:
    def __init__(self) :
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self) :
        self.root = TrieNode()

    def insert(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True
    