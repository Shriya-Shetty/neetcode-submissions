class WordDictionary:
    def __init__(self):
        self.children = {}
        self.end_of_word = False        

    def addWord(self, word: str) -> None:
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = WordDictionary()
            node = node.children[c]
        node.end_of_word = True   # mark the last node

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.end_of_word
            c = word[i]
            if c == '.':
                # try all children
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                if c not in node.children:
                    return False
                return dfs(node.children[c], i + 1)

        return dfs(self, 0)
