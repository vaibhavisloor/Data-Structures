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
    
    def search(self, word):
        node = self.root
        for char in word:  # Iterate over the characters of the word
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end_of_word
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:  # Iterate over the characters of the prefix
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
if __name__ == "__main__":
    # Create a Trie instance
    trie = Trie()

    # Insert words into the Trie
    trie.insert("cat")
    trie.insert("car")
    trie.insert("dog")
    trie.insert("dart")

    # Search for words
    print(trie.search("cat"))    # Output: True
    print(trie.search("can"))    # Output: False

    # Check for prefixes
    print(trie.starts_with("ca"))  # Output: True
    print(trie.starts_with("do"))  # Output: True
    print(trie.starts_with("dar")) # Output: True
    print(trie.starts_with("dan")) # Output: False