#Trie = a tree used to store words character by character

# trienode

class TrieNode:
    def __init__(self):
        self.children={}#stores next characters
        self.is_end=False #tells us a word ends here

#trie
class Trie:
    def __init__(self):
        self.root=TrieNode() #starting point

#insert
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

        node.is_end =True
# Search
    def search(self , word ):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False

            node = node.children[ch]
        return node.is_end
trie = Trie()
trie.insert("car")

m=trie.search("car")
print(m)