class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.is_end_of_word = True
    
    def search(self, word):
        current = self.root
        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]
        return current.is_end_of_word
    
    def starts_with(self, prefix):
        current = self.root
        for c in prefix:
            if c not in current.children:
                return []
            current = current.children[c]
        return self._find_words(current, prefix)
    
    def _find_words(self, node, prefix):
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for c, child in node.children.items():
            words.extend(self._find_words(child, prefix + c))
        return words
