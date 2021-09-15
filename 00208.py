class Trie:

    def __init__(self):
        self.root = TrieNode(False)

    def insert(self, word: str) -> None:
        node = self.root
        for i, w in enumerate(word):
            node = node.insert(w, (i == len(word)-1))

    def search(self, word: str) -> bool:
        node = self.root
        for i, w in enumerate(word):
            if node is None:
                return False
            if w not in node.nodes:
                return False
            if i == len(word)-1:
                return node.nodes[w].last
            node = node.nodes[w]
        return False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for w in prefix:
            if node is None:
                return False
            if w not in node.nodes:
                return False
            node = node.nodes[w]
        return True

class TrieNode:
    def __init__(self, last):
        self.last = last
        self.nodes = dict()

    def insert(self, c, last):
        if c in self.nodes:
            if last == True:
                self.nodes[c].last = last
        else:
            self.nodes[c] = TrieNode(last)
        return self.nodes[c]

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# ["Trie","insert","insert","insert","insert","insert","insert","search","search","search","search","search","search","search","search","search","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith"]
# [[],["app"],["apple"],["beer"],["add"],["jam"],["rental"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"]]
# [null,null,null,null,null,null,null,false,true,false,false,false,false,false,true,true,false,true,true,false,false,true,true,true,true]
# [null,null,null,null,null,null,null,false,true,false,false,false,false,false,true,true,false,true,true,false,false,false,true,true,true]

trie = Trie()

trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")

print(trie.search("app"))
